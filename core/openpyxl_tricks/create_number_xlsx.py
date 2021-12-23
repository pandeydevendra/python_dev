from openpyxl import Workbook

wb = Workbook()
random_numbers = wb.active

wb.save('number.xlsx')
