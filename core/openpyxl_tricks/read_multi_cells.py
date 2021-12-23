import openpyxl

wb_load = openpyxl.load_workbook('item.xlsx')
sheet = wb_load.active

cells = sheet['A1': 'B6']

print(cells)
'''
o/p: ((<Cell 'Sheet'.A1>, <Cell 'Sheet'.B1>), (<Cell 'Sheet'.A2>, <Cell 'Sheet'.B2>),
 (<Cell 'Sheet'.A3>, <Cell 'Sheet'.B3>), (<Cell 'Sheet'.A4>, <Cell 'Sheet'.B4>), 
 (<Cell 'Sheet'.A5>, <Cell 'Sheet'.B5>), (<Cell 'Sheet'.A6>, <Cell 'Sheet'.B6>))

'''
# print(cells.value)
# AttributeError: 'tuple' object has no attribute 'value'

for c1, c2 in cells:
    print(c1.value, c2.value)

for c1, c2 in cells:
    print("{0:1} {1:1}".format(c1.value, c2.value))

for c1, c2 in cells:
    print("{0:5} {1:5}".format(c1.value, c2.value))

for c1, c2 in cells:
    print("{0:10} {1:10}".format(c1.value, c2.value))
