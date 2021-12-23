from openpyxl import Workbook

wb = Workbook()
sheet = wb.active

rows = (
    (88, 46, 57),
    (89, 38, 12),
    (23, 59, 78),
    (56, 21, 98),
    (24, 18, 43),
    (34, 15, 67)
)

for row in rows:
    sheet.append(row)

wb.save('appending.xlsx')


"""
The data is stored in a tuple of tuples.

for row in rows:
    sheet.append(row)
We go through the container row by row and insert the data row with the append method.
"""