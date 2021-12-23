from openpyxl import Workbook

wb = Workbook()
sheet = wb.active

rows = (
    ('Item', 'Quantity'),
    ('coins', 23),
    ('chairs', 3),
    ('pencils', 5),
    ('bottles', 8),
    ('books', 30)
)

for row in rows:
    sheet.append(row)

wb.save('item.xlsx')
