import openpyxl

wb_load = openpyxl.load_workbook('sheets.xlsx')

print(wb_load.get_sheet_names())
active_sheet = wb_load.active
print(type(active_sheet))

sheet = wb_load.get_sheet_by_name("March")
print(sheet.title)
print(wb_load.sheetnames)
