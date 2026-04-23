import sqlite3
c = sqlite3.connect('amazon_offers_history.db')
c.row_factory = sqlite3.Row
rows = c.execute("SELECT variant_name, image_url FROM cheapest_offers_history ORDER BY id DESC LIMIT 10").fetchall()
for r in rows:
    if 'Xbox' in r['variant_name']:
        print(dict(r))
