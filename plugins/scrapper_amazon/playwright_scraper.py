import csv
import json
import hashlib
from playwright.sync_api import sync_playwright
import os

# Determina caminhos absolutos relativos ao executado
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CSV_PATH = os.path.join(BASE_DIR, "search_terms.csv")
JSON_OUTPUT = os.path.join(BASE_DIR, "amazon_classified.json")

def calculate_hash(row_text):
    return hashlib.sha256(row_text.encode('utf-8')).hexdigest()

def scrape_with_playwright():
    classified = {}
    
    if not os.path.exists(CSV_PATH):
        print(f"CSV de referências nao encontrado: {CSV_PATH}")
        return

    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        terms = list(reader)

    # Inicia a máquina de navegação autônoma
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            locale="pt-BR"
        )
        page = context.new_page()

        for term in terms:
            spec = term['product_name_spec']
            cat = term['category']
            row_id = term['id']
            
            if cat not in classified:
                classified[cat] = []
            
            print(f"Buscando autonomamente: {spec}...")
            import urllib.parse
            encoded_spec = urllib.parse.quote_plus(spec)
            search_url = f"https://www.amazon.com.br/s?k={encoded_spec}"
            
            try:
                # Carrega o esqueleto DOM.
                page.goto(search_url, wait_until="domcontentloaded", timeout=20000)
                page.screenshot(path="debug_amazon.png")
                
                try:
                    page.wait_for_selector('[data-component-type="s-search-result"]', timeout=8000)
                except:
                    print(" -> Sem resultados rendrizados na Amazon a tempo (talvez esgotado ou capctha).")
                    continue
                
                results = page.locator('[data-component-type="s-search-result"]')
                count = results.count()
                
                if count > 0:
                    with open("debug_amazon.html", "w", encoding="utf-8") as f:
                        f.write(results.nth(2).inner_html()) # Pula os dois primeiros caso sejam patrocinados pra teste
                
                best_item = None
                
                # Varre os itens da grade até achar um Orgânico Real
                for i in range(count):
                    loc = results.nth(i)
                    
                    # Checamos o flag de class do adsense nativo
                    sponsored = loc.locator('.puis-sponsored-label-text, .puis-sponsored-label-info-icon').count() > 0
                    if sponsored:
                        continue
                        
                    title_loc = loc.locator('[data-cy="title-recipe"] h2').first
                    link_loc = loc.locator('[data-cy="title-recipe"] a.a-link-normal').first
                    
                    if title_loc.count() == 0 or link_loc.count() == 0:
                        continue
                        
                    title = title_loc.text_content().strip()
                    url = link_loc.get_attribute("href")
                    if url and not url.startswith("http"):
                        url = "https://www.amazon.com.br" + url
                        
                    price_str = None
                    text_content = loc.text_content()
                    import re
                    match = re.search(r'R\$\s?([\d\.,]+)', text_content)
                    if match:
                        price_str = f"R$ {match.group(1).strip()}"
                        
                    image_loc = loc.locator('img.s-image').first
                    img_url = image_loc.get_attribute("src") if image_loc.count() > 0 else ""
                    
                    if price_str:
                        # Amarração Oculta para BD Histórico: Hash absoluto da linha no CSV
                        row_hash = calculate_hash(f"{row_id},{cat},{spec}")
                        
                        best_item = {
                            "title": title,
                            "url": url,
                            "price": price_str,
                            "image": img_url,
                            "csv_hash_id": row_hash,
                            "target_query": spec
                        }
                        # Como estamos ordenando por relevância da própria Amazon, 
                        # o 1º orgânico geralmente é o item oficial buscado (a busca inteligente garante isso).
                        break 
                        
                if best_item:
                    classified[cat].append(best_item)
                    print(f" -> Encontrado e Hash Gerado: {best_item['price']} | {best_item['csv_hash_id'][:8]} | {best_item['title'][:40]}...")
                else:
                    print(f" -> Nenhum resultado orgânico viável extraído.")
                    
            except Exception as e:
                print(f" -> Erro no pipeline para '{spec}': {e}")

        browser.close()
        
    with open(JSON_OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(classified, f, ensure_ascii=False, indent=4)
        
    print(f"\nFinalizado de forma limpa! Nova geração mapeada de produtos listada em: amazon_classified.json")

if __name__ == "__main__":
    scrape_with_playwright()
