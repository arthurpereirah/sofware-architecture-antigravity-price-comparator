import json
try:
    with open("amazon_products_local.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    for i in data:
        if i.get("sku_amazon") == "XBOX1_MOCK":
            i["image"] = "https://m.media-amazon.com/images/I/61z3GQgEPZL._AC_SL1500_.jpg"
            i["url"] = "https://www.amazon.com.br/dp/B08K34Z2XQ"
        elif i.get("sku_amazon") == "XBOXCTRL_MOCK":
            i["image"] = "https://m.media-amazon.com/images/I/61KNJixB3wL._AC_SL1500_.jpg"
            i["url"] = "https://www.amazon.com.br/dp/B08DF248LD"
    with open("amazon_products_local.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
except Exception as e:
    print(e)
