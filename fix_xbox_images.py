import json

try:
    with open("amazon_products_local.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    for i in data:
        if i.get("sku_amazon") == "XBOX1_MOCK":
            i["image"] = "https://m.media-amazon.com/images/I/51W1h2O64aL._AC_SL1000_.jpg"
            i["url"] = "https://www.amazon.com.br/dp/B0D932YWSZ"
        elif i.get("sku_amazon") == "XBOXCTRL_MOCK":
            i["image"] = "https://m.media-amazon.com/images/I/61U0Tz2969L._AC_SL1500_.jpg"
            i["url"] = "https://www.amazon.com.br/dp/B09BYL7M6N"
    with open("amazon_products_local.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
except Exception as e:
    print(e)
