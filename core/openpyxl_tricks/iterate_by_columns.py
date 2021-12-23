from openpyxl import Workbook

wb = Workbook()
sheet = wb.active

tuple_data = (
    (88, 46, 57),
    (89, 38, 12),
    (23, 59, 78),
    (56, 21, 98),
    (24, 18, 43),
    (34, 15, 67)
)

for tuple in tuple_data:
    sheet.append(tuple)

for col in sheet.iter_cols(min_col=1, max_col=3, min_row=1, max_row=6, ):
    for cell in col:
        print(cell.value, end=" ")
    print()

wb.save('iterate_by_cols.xlsx')