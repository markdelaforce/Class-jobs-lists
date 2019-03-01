from lists_page import *
    
options_page = Tk()
options_page.title("Class jobs")
options_page.geometry('1440x800+0+0')
options_page.resizable(width=FALSE, height=FALSE)

header_font = font.Font(family='comic sans ms', size=60, weight='bold')
button_font = font.Font(family='comic sans ms', size=28, weight='bold')

header = Label(options_page, text="Class Jobs", bg='#ffd166', fg='#ef476f', width='40', height='2', font=header_font).pack()
Label(options_page, height=7).pack()

button_bar_1 = Frame(options_page)
button_bar_1.pack()

button_1 = Label(button_bar_1, text='Monday 4.15', bg='#a69658', fg='#fff480', font=button_font, width=15, bd=4, relief='raised')
button_1.pack(side=LEFT)
button_1.bind("<Button-1>", lambda event: display_class_lists(event, class_index=0))

Label(button_bar_1, width=15).pack(side=LEFT)

button_2 = Label(button_bar_1, text='Wednesday 3.20', bg='#a69658', fg='#fff480', font=button_font, width=15, bd=4, relief='raised')
button_2.pack(side=LEFT)
button_2.bind("<Button-1>", lambda event: display_class_lists(event, class_index=1))

Label(options_page, height=5).pack()

button_bar_2 = Frame(options_page)
button_bar_2.pack()

button_3 = Label(button_bar_2, text='Thursday 4.00', bg='#a69658', fg='#fff480', font=button_font, width=15, bd=4, relief='raised')
button_3.pack(side=LEFT)
button_3.bind("<Button-1>", lambda event: display_class_lists(event, class_index=2))

Label(button_bar_2, width=15).pack(side=LEFT)

button_4 = Label(button_bar_2, text='Thursday 5.15', bg='#a69658', fg='#fff480', font=button_font, width=15, bd=4, relief='raised')
button_4.pack(side=LEFT)
button_4.bind("<Button-1>", lambda event: display_class_lists(event, class_index=3))

options_page.mainloop()

os.system("cls" if os.name == "nt" else "clear")