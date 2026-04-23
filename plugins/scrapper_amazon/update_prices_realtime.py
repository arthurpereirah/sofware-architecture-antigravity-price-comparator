import json
import urllib.request
import re
import time
import random
import os

def fetch_live_price(url: str) -> str:
    if "amazon.com.br" not in url:
        return None
        
    try:
        # Give a small human-like delay to avoid getting slammed by Captchas
        time.sleep(random.uniform(0.5, 1.5))
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        })
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        
        # Procura o preço no formato brasileiro R$ XXX,XX ou extrai a parte inteira e fracionária
        price_whole = re.search(r'class="a-price-whole"[^>]*>([^<]+)<', html)
        price_fraction = re.search(r'class="a-price-fraction"[^>]*>([^<]+)<', html)
        
        if price_whole:
            whole = price_whole.group(1).replace(".", "").replace(",", "").strip() # Remove pontuações ruidosas
            frac = price_fraction.group(1).strip() if price_fraction else "00"
            # Format cleanly to our system standard
            return f"R$ {whole},{frac}"
            
        return None
    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")
        return None

def update_catalog(file_path="amazon_classified.json"):
    print("🔄 INICIANDO ATUALIZAÇÃO EM TEMPO REAL DOS PREÇOS (BYPASS DE CAPTCHA)...")
    if not os.path.exists(file_path):
        print(f"Arquivo {file_path} não encontrado.")
        return
        
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    updated_count = 0
    total_count = 0
    for category, items in data.items():
        for i, item in enumerate(items):
            total_count += 1
            url = item.get("url")
            old_price = item.get("price")
            
            if not url:
                continue
                
            print(f"[{total_count}] Checando: {item.get('title')[:30]}...")
            new_price = fetch_live_price(url)
            
            if new_price and new_price != old_price:
                print(f"   📉 Preço Atualizado! DE: {old_price} PARA: {new_price}")
                item["price"] = new_price
                updated_count += 1
            elif not new_price:
                print(f"   ⚠️ Produto indisponível ou captchado. Mantendo preço atual.")
                
    if updated_count > 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"✅ {updated_count} valores atualizados com sucesso e salvos no JSON base!")
    else:
        print("✅ Dados verificados. Nenhum valor novo detectado na loja.")

if __name__ == "__main__":
    update_catalog()
