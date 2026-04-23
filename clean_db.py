import sqlite3
conn = sqlite3.connect('amazon_offers_history.db')
c = conn.cursor()
c.execute("DELETE FROM cheapest_offers_history WHERE variant_name IN ('Console Xbox One', 'Console Xbox 360', 'Controle Xbox Elite')")
conn.commit()
conn.close()
print("Limpeza do DB concluida com sucesso!")
