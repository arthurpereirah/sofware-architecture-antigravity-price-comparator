import json

img1 = "https://m.media-amazon.com/images/I/51W1h2O64aL._AC_SL1000_.jpg" # Xbox Console (Amazon Media Server)
img2 = "https://m.media-amazon.com/images/I/61U0Tz2969L._AC_SL1500_.jpg" # Elite Controller (Amazon Media Server)

with open('amazon_classified.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for category, items in data.items():
    for item in items:
        if 'Xbox One S' in item.get('title', ''):
            item['image'] = img1
        elif 'Elite' in item.get('title', '') and 'Xbox' in item.get('title', ''):
            item['image'] = img2

with open('amazon_classified.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Imagens atualizadas com sucesso para os servidores da Amazon!")
