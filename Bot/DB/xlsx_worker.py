import os

from datetime import datetime
from openpyxl import Workbook

file_path = 'result/price_data.xlsx'

def check_path():
    dir = os.path.dirname(file_path)
    if not os.path.exists(dir):
        os.makedirs(dir)

def write_to_excel(data):
    check_path()
    wb = Workbook()
    ws = wb.active
    ws.append(['ID', 'Date', 'Time', 'Price'])

    for row in data:
        ws.append(row)

    wb.save(file_path)

if __name__ == "__main__":
    from db import get_data_by_date
    write_to_excel(get_data_by_date())