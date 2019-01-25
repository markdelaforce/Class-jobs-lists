from tkinter import *
from tkinter import font
import os

def increase_var(event=None, var=''):
    this.var.set(var.get()+1)

window = Tk()
window.title("test")
window.geometry('1440x800')
window.resizable(width=FALSE, height=FALSE)

header_font = font.Font(family='comic sans ms', size=60, weight='bold')
button_font = font.Font(family='comic sans ms', size=20, weight='bold')
info_font = font.Font(family='comic sans ms', size=22, weight='bold')

header = Label(window, text="Test app", bg='#ffd166', fg='#ef476f', width='40', height='2', font=header_font).pack()
Label(window, height=7).pack()

x = IntVar()
x.set(1)
y = IntVar()
y.set(1)
z = IntVar()
z.set(1)
values = [x, y, z]

for index in range(3):
    buttons = Label(window, text='Button ' + str(index+1), height=3, width=20, bg='cyan', font=info_font)
    buttons.pack()
    buttons.bind('<Button-1>', lambda event: increase_var(event, var=values[index])) 
    labels = Label(window, textvariable=values[index], height=2, width=20, font=info_font)
    labels.pack()

window.mainloop()

os.system("cls" if os.name == "nt" else "clear")