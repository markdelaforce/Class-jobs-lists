from lists_page import *

def buttonBar(holder):
    button_bar = Frame(holder)
    button_bar.pack()
    button_bar.configure(background=backgroundColour)
    return button_bar
    
def button(holder, string, index):
    button = Label(holder, text=string, bg=buttonBackground, fg=buttonText, font=button_font, width=15, bd=4, relief='raised')
    button.pack(side=LEFT)
    button.bind("<Button-1>", lambda event: display_class_lists(event, class_index=index))
    return button

backgroundColour = '#fcf8e8'
buttonBackground = '#635380'
buttonText = '#ddd78d'
    
options_page = Tk()
options_page.title("Class jobs")
options_page.geometry('1440x800+0+0')
options_page.resizable(width=FALSE, height=FALSE)
options_page.configure(background=backgroundColour)

header_font = font.Font(family='comic sans ms', size=60, weight='bold')
button_font = font.Font(family='comic sans ms', size=28, weight='bold')

header = Label(options_page, text="Class Jobs", bg='#a5668b', fg='#97c7ce', width='40', height='2', font=header_font).pack()
Label(options_page, height=7, background=backgroundColour).pack()

button_bar_1 = buttonBar(options_page)
button_1 = button(button_bar_1, 'Monday 4.15', 0)
Label(button_bar_1, width=15, background=backgroundColour).pack(side=LEFT)
button_2 = button(button_bar_1, 'Monday 5.30', 1)
Label(button_bar_1, width=15, background=backgroundColour).pack(side=LEFT)
button_3 = button(button_bar_1, 'Tuesday 4.00', 2)

Label(options_page, height=5, background=backgroundColour).pack()

button_bar_2 = buttonBar(options_page)
button_4 = button(button_bar_2, 'Tuesday 5.15', 3)
Label(button_bar_2, width=15, background=backgroundColour).pack(side=LEFT)
button_5 = button(button_bar_2, 'Wednesday 5.00', 4)
Label(button_bar_2, width=15, background=backgroundColour).pack(side=LEFT)
button_6 = button(button_bar_2, 'Wednesday 6.15', 5)

Label(options_page, height=5, background=backgroundColour).pack()

button_bar_3 = buttonBar(options_page)
button_7 = button(button_bar_3, 'Thursday 5.30', 6)
Label(button_bar_3, width=15, background=backgroundColour).pack(side=LEFT)
button_8 = button(button_bar_3, 'Thursday 6.30', 7)
Label(button_bar_3, width=15, background=backgroundColour).pack(side=LEFT)
button_9 = button(button_bar_3, 'Friday 4.15', 8)

options_page.mainloop()

os.system("cls" if os.name == "nt" else "clear")
