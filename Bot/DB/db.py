import sqlite3
from datetime import datetime
from DB.scrap import Scraper

def create_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS PriceData (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date TEXT,
                        time TEXT,
                        price TEXT)''')

def insert_data(cursor, price):
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")
    cursor.execute("INSERT INTO PriceData (date, time, price) VALUES (?, ?, ?)", (current_date, current_time, price))

def add_data():
    scraper = Scraper()
    price = scraper.search_price()

    conn = sqlite3.connect('price_data.db')
    cursor = conn.cursor()

    create_table(cursor)
    insert_data(cursor, price)
    
    conn.commit()
    conn.close()

def get_data_by_date():
    conn = sqlite3.connect('price_data.db')
    cursor = conn.cursor()

    date_str = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("SELECT * FROM PriceData WHERE date(date) = ?", (date_str,))
    data = cursor.fetchall()

    conn.close()
    return data

if __name__ == "__main__":
    add_data()
    data_today = get_data_by_date()

    print("Данные за сегодня:")
    for row in data_today:
        print(row)
    