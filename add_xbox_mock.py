import json
try:
    with open("amazon_products_local.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    if not any("Xbox" in i.get("title","") for i in data):
        data.append({
            "sku_amazon": "XBOX1_MOCK",
            "title": "Microsoft Console Xbox One S 500GB",
            "price_current": "R$ 1.900,00",
            "price_original": "R$ 2.200,00",
            "rating": "4.5",
            "reviews_count": "100",
            "sales_info": "-",
            "sponsored": "Não",
            "is_prime": "Sim",
            "delivery": "-",
            "image": "",
            "url": "https://www.amazon.com.br"
        })
        data.append({
            "sku_amazon": "XBOXCTRL_MOCK",
            "title": "Controle Xbox Series Elite",
            "price_current": "R$ 800,00",
            "price_original": "R$ 800,00",
            "rating": "4.9",
            "reviews_count": "200",
            "sales_info": "-",
            "sponsored": "Não",
            "is_prime": "Sim",
            "delivery": "-",
            "image": "",
            "url": "https://www.amazon.com.br"
        })
        with open("amazon_products_local.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("Mocks inseridos!")
    else:
        print("Mocks já existem!")
except Exception as e:
    print(e)
