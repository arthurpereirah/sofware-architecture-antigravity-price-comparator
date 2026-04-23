import urllib.request, re, json

def get_img(query):
    req = urllib.request.Request(f'https://www.amazon.com.br/s?k={query}', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    match = re.search(r'https://m\.media-amazon\.com/images/I/[^\"]+?\.jpg', html)
    return match.group(0) if match else "https://m.media-amazon.com/images/I/51r5zH40ePL._AC_UL320_.jpg"

img1 = get_img('xbox+one+s+console')
img2 = get_img('xbox+elite+controller')

# Replace in amazon_classified.json
with open('amazon_classified.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for category in data.values():
    for item in category:
        if 'Xbox One S' in item.get('title', ''):
            item['image'] = img1
        elif 'Elite' in item.get('title', '') and 'Xbox' in item.get('title', ''):
            item['image'] = img2

with open('amazon_classified.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Images updated:", img1, img2)
