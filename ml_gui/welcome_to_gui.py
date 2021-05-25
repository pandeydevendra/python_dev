# GUI: Graphical User Interface..............

import PySimpleGUI as sg

output = [[sg.Text("Enter Your name...")], [sg.Input()], [sg.Button('Ok')]]
window = sg.Window('Window Title', output)
program, data = window.read()
print('Hello', data[0], "! \nWelcome to the PySimpleGUI world.")
window.close()
