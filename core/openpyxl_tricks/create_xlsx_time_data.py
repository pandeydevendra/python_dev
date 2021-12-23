# Openpyxl create new file

from openpyxl import Workbook
import time

book = Workbook()
sheet = book.active

sheet['A1'] = 'Date'
now = time.strftime("%x")
sheet['B1'] = now

sheet['A2'] = 'mayank'
sheet['A3'] = 'rohan'
sheet['B2'] = 100
sheet['B3'] = 200

book.save("data_time_sample_00.xlsx")

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

now = time.strftime("%x")
sheet['A3'] = now
We write current date to the cell A3.

book.save("sample.xlsx")
We write the contents to the sample.xlsx file with the save method.
"""
