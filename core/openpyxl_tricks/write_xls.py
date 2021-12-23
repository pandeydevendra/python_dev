# Openpyxl create new file

from openpyxl import Workbook

book = Workbook()
sheet = book.active

sheet['A1'] = 56
sheet['A2'] = 43

book.save("sample_01.xlsx")

"""
In the example, we create a new xlsx file. We write data into two cells.

from openpyxl import Workbook
From the openpyxl module, we import the Workbook class. 
A workbook is the container for all other parts of the document.

book = Workbook()
We create a new workbook. A workbook is always created with at least one worksheet.

sheet = book.active
We get the reference to the active sheet.

sheet['A1'] = 56
sheet['A2'] = 43
We write numerical data to cells A1 and A2.

book.save("sample.xlsx")
We write the contents to the sample.xlsx file with the save method.
"""
