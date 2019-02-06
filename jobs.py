from lists_page import *
    
options_page = Tk()
options_page.geometry('1440x800+0+0')
options_page.resizable(width=FALSE, height=FALSE)

button_1 = Label(options_page, text='Button 1')
button_1.pack()
button_1.bind("<Button-1>", lambda event: display_class_lists(event, class_index=0))

button_2 = Label(options_page, text='Button 2')
button_2.pack()
button_2.bind("<Button-1>", lambda event: display_class_lists(event, class_index=1))

options_page.mainloop()

os.system("cls" if os.name == "nt" else "clear")