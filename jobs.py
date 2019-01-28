from tkinter import *
from tkinter import font
import datetime
import os

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def load_list(directory, filename, display_names, display_dates, text_file_names, text_file_dates):
    os.chdir(directory)
    open_file = open(filename, 'r')
    next_line = open_file.readline()
    for child in range(class_size.get()):
        data = next_line.strip().split(',')
        text_file_names.append(data[0])
        text_file_dates.append(data[1])
        next_line = open_file.readline()
    open_file.close()
    for index in range(class_size.get()):
        display_names[index].set(text_file_names[index])
        date_elements = text_file_dates[index].split('-')
        date = date_elements[2] + ' ' + months[int(date_elements[1])-1]
        display_dates[index].set(date)
    os.chdir('..')

def print_lists():
    file_names = ['names.txt', 'jasper.txt', 'computer.txt', 'whiteboard.txt']
    all_names = [file_list_names, file_jasper_names, file_computer_names, file_whiteboard_names]
    all_dates = [file_list_dates, file_jasper_dates, file_computer_dates, file_whiteboard_dates]
    for outer_index in range(len(file_names)):
        print(file_names[outer_index])
        for dash in range(len(file_names[outer_index])):
            print('-', end='')
        print()
        for inner_index in range(len(all_names[outer_index])):
            print(all_names[outer_index][inner_index] + ',' + all_dates[outer_index][inner_index])
        print()
        
def updating_list():
    if list_update_status.get() == 'update':
        return True
    elif jasper_update_status.get() == 'update':
        return True
    elif computer_update_status.get() == 'update':
        return True
    elif whiteboard_update_status.get() == 'update':
        return True
    return False
    
def choose_next_person(event=None, update_status='', next_name='', file_names=[], file_dates=[], _index=0, display_names=[], display_dates=[], filename=''):
    if not updating_list():
        update_status.set('update')
        for index in range(4):
            if all_update_statuses[index].get() == 'update':
                all_buttons_text[index].set('select')
            else:
                all_buttons_text[index].set('')
        next_name.set(file_names[0])
    elif update_status.get() == 'update':
        next_name.set('')
        file_names.append(file_names.pop(_index.get()))
        file_dates.pop(_index.get())
        file_dates.append(str(datetime.datetime.now()).split()[0])
        for index in range(len(file_names)):
            display_names[index].set(file_names[index])
            date_elements = file_dates[index].split('-')
            display_dates[index].set(date_elements[2] + ' ' + months[int(date_elements[1])-1])
        _index.set(0)         
        names_file = open(filename, 'w')
        for index in range(len(file_names)):
            names_file.write(str(file_names[index]) + ',' + str(file_dates[index]) + '\n')
        names_file.close()
        update_status.set('initial')
        for index in range(4):
            all_buttons_text[index].set('choose next')
        
def next_name(event):
    if list_update_status.get() == 'update' and list_index.get() < class_size.get()-1:
        list_index.set(list_index.get()+1)
        list_next_name.set(file_list_names[list_index.get()])
    elif jasper_update_status.get() == 'update' and jasper_index.get() < class_size.get()-1:
        jasper_index.set(jasper_index.get()+1)
        jasper_next_name.set(file_jasper_names[jasper_index.get()])    
    elif computer_update_status.get() == 'update' and computer_index.get() < class_size.get()-1:
        computer_index.set(computer_index.get()+1)
        computer_next_name.set(file_computer_names[computer_index.get()])
    elif whiteboard_update_status.get() == 'update' and whiteboard_index.get() < class_size.get()-1:
        whiteboard_index.set(whiteboard_index.get()+1)
        whiteboard_next_name.set(file_whiteboard_names[whiteboard_index.get()])

def last_name(event):
    if list_update_status.get() == 'update' and list_index.get() > 0:
        list_index.set(list_index.get()-1)
        list_next_name.set(file_list_names[list_index.get()])
    elif jasper_update_status.get() == 'update' and jasper_index.get() > 0:
        jasper_index.set(jasper_index.get()-1)
        jasper_next_name.set(file_jasper_names[jasper_index.get()])
    elif computer_update_status.get() == 'update' and computer_index.get() > 0:
        computer_index.set(computer_index.get()-1)
        computer_next_name.set(file_computer_names[computer_index.get()])
    elif whiteboard_update_status.get() == 'update' and whiteboard_index.get() > 0:
        whiteboard_index.set(whiteboard_index.get()-1)
        whiteboard_next_name.set(file_whiteboard_names[whiteboard_index.get()])

    
window = Tk()
window.title("Class jobs")
window.geometry('1440x800')
window.resizable(width=FALSE, height=FALSE)

class_index = 0
class_sizes = [7, 4]
class_size = IntVar()
class_size.set(class_sizes[class_index])
classes = ['Monday_4', 'Thursday_4']
class_ref = classes[class_index]

header_font = font.Font(family='comic sans ms', size=60, weight='bold')
title_font = font.Font(family='comic sans ms', size=28, weight='bold')
general_font = font.Font(family='comic sans ms', size=22, weight='bold')

header = Label(window, text="Class Jobs", bg='#ffd166', fg='#ef476f', width='40', height='2', font=header_font).pack()
Label(window, height=7).pack()

footer_frame = Frame(window, pady=55)
footer_frame.pack(side=BOTTOM)
buttons = Frame(footer_frame)
buttons.pack()
next_name_display = Frame(footer_frame)
next_name_display.pack()

button_1_text = StringVar()
button_1_text.set('choose next')
button_2_text = StringVar()
button_2_text.set('choose next')
button_3_text = StringVar()
button_3_text.set('choose next')
button_4_text = StringVar()
button_4_text.set('choose next')
all_buttons_text = [button_1_text, button_2_text, button_3_text, button_4_text]

list_update_status = StringVar()
list_update_status.set('initial')
list_next_name = StringVar()
list_index = IntVar()
list_index.set(0)
list_button = Label(buttons, textvariable=button_1_text, font=general_font, bg='#a69658', fg='#fff480', width=12, bd=4, relief='raised')
list_button.pack(side=LEFT)
list_button.bind("<Button-1>", lambda event: choose_next_person(event,
update_status=list_update_status,
next_name=list_next_name,
file_names=file_list_names,
file_dates=file_list_dates,
_index=list_index,
display_names=display_names_1,
display_dates=display_dates_1,
filename='list.txt'))
list_next_display = Label(next_name_display, textvariable=list_next_name, width=12, font=general_font, pady=10, fg='#f0386b', bd=4, relief='flat').pack(side=LEFT)

Label(buttons, width=23).pack(side=LEFT)
Label(next_name_display, width=23).pack(side=LEFT)

jasper_update_status = StringVar()
jasper_update_status.set('initial')
jasper_next_name = StringVar()
jasper_index = IntVar()
jasper_index.set(0)
jasper_button = Label(buttons, textvariable=button_2_text, font=general_font, bg='#a69658', fg='#fff480', width=12, bd=4, relief='raised')
jasper_button.pack(side=LEFT)
jasper_button.bind("<Button-1>", lambda event: choose_next_person(event,
update_status=jasper_update_status,
next_name=jasper_next_name,
file_names=file_jasper_names,
file_dates=file_jasper_dates,
_index=jasper_index,
display_names=display_names_2,
display_dates=display_dates_2,
filename='jasper.txt'))
jasper_next_display = Label(next_name_display, textvariable=jasper_next_name, width=12, font=general_font, pady=10, fg='#f0386b', bd=4, relief='flat').pack(side=LEFT)

Label(buttons, width=23).pack(side=LEFT)
Label(next_name_display, width=23).pack(side=LEFT)

computer_update_status = StringVar()
computer_update_status.set('initial')
computer_next_name = StringVar()
computer_index = IntVar()
computer_index.set(0)
computer_button = Label(buttons, textvariable=button_3_text, font=general_font, bg='#a69658', fg='#fff480', width=12, bd=4, relief='raised')
computer_button.pack(side=LEFT)
computer_button.bind("<Button-1>", lambda event: choose_next_person(event,
update_status=computer_update_status,
next_name=computer_next_name,
file_names=file_computer_names,
file_dates=file_computer_dates,
_index=computer_index,
display_names=display_names_3,
display_dates=display_dates_3,
filename='computer.txt'))
computer_next_display = Label(next_name_display, textvariable=computer_next_name, width=12, font=general_font, pady=10, fg='#f0386b', bd=4, relief='flat').pack(side=LEFT)

Label(buttons, width=23).pack(side=LEFT)
Label(next_name_display, width=23).pack(side=LEFT)

whiteboard_update_status = StringVar()
whiteboard_update_status.set('initial')
whiteboard_next_name = StringVar()
whiteboard_index = IntVar()
whiteboard_index.set(0)
whiteboard_button = Label(buttons, textvariable=button_4_text, font=general_font, bg='#a69658', fg='#fff480', width=12, bd=4, relief='raised')
whiteboard_button.pack(side=LEFT)
whiteboard_button.bind("<Button-1>", lambda event: choose_next_person(event,
update_status=whiteboard_update_status,
next_name=whiteboard_next_name,
file_names=file_whiteboard_names,
file_dates=file_whiteboard_dates,
_index=whiteboard_index,
display_names=display_names_4,
display_dates=display_dates_4,
filename='whiteboard.txt'))
whiteboard_next_display = Label(next_name_display, textvariable=whiteboard_next_name, width=12, font=general_font, pady=10, fg='#f0386b', bd=4, relief='flat').pack(side=LEFT)


all_update_statuses = [list_update_status, jasper_update_status, computer_update_status, whiteboard_update_status]

window.bind("<Down>", next_name)
window.bind("<Up>", last_name)

# -------------------------------------------------------------------------------------------------

Label(window, width=3).pack(side=LEFT)

file_list_names = []
file_list_dates = []

name1_1 = StringVar()
name2_1 = StringVar()
name3_1 = StringVar()
name4_1 = StringVar()
name5_1 = StringVar()
name6_1 = StringVar()
name7_1 = StringVar()

date1_1 = StringVar()
date2_1 = StringVar()
date3_1 = StringVar()
date4_1 = StringVar()
date5_1 = StringVar()
date6_1 = StringVar()
date7_1 = StringVar()

display_names_1 = [name1_1, name2_1, name3_1, name4_1, name5_1, name6_1, name7_1]
display_dates_1 = [date1_1, date2_1, date3_1, date4_1, date5_1, date6_1, date7_1]

list_frame_1 = Frame(window)
list_frame_1.pack(side=LEFT)

Label(list_frame_1, text='Names List', font=title_font, fg='#f46036', pady=5, padx=5, width=18, bg='#f9f1d2').pack(side=TOP)

person_1_1 = Frame(list_frame_1)
person_2_1 = Frame(list_frame_1)
person_3_1 = Frame(list_frame_1)
person_4_1 = Frame(list_frame_1)
person_5_1 = Frame(list_frame_1)
person_6_1 = Frame(list_frame_1)
person_7_1 = Frame(list_frame_1)

list_1 = [person_1_1, person_2_1, person_3_1, person_4_1, person_5_1, person_6_1, person_7_1]

for index in range(class_size.get()):
    next_person_1 = list_1[index]
    next_person_1.pack(side=TOP, fill=X)
    Label(next_person_1, textvariable=display_names_1[index], font=general_font, fg='#3066be').pack(side=LEFT)
    Label(next_person_1, width=5).pack(side=LEFT)
    Label(next_person_1, textvariable=display_dates_1[index], font=general_font, fg='#009973').pack(side=RIGHT)
    
# -------------------------------------------------------------------------------------------------

Label(window, width=3).pack(side=LEFT)

file_jasper_names = []
file_jasper_dates = []

name1_2 = StringVar()
name2_2 = StringVar()
name3_2 = StringVar()
name4_2 = StringVar()
name5_2 = StringVar()
name6_2 = StringVar()
name7_2 = StringVar()

date1_2 = StringVar()
date2_2 = StringVar()
date3_2 = StringVar()
date4_2 = StringVar()
date5_2 = StringVar()
date6_2 = StringVar()
date7_2 = StringVar()

display_names_2 = [name1_2, name2_2, name3_2, name4_2, name5_2, name6_2, name7_2]
display_dates_2 = [date1_2, date2_2, date3_2, date4_2, date5_2, date6_2, date7_2]

list_frame_2 = Frame(window)
list_frame_2.pack(side=LEFT)

Label(list_frame_2, text='Jasper', font=title_font, fg='#f46036', pady=5, padx=5, width=18, bg='#f9f1d2').pack(side=TOP)

person_1_2 = Frame(list_frame_2)
person_2_2 = Frame(list_frame_2)
person_3_2 = Frame(list_frame_2)
person_4_2 = Frame(list_frame_2)
person_5_2 = Frame(list_frame_2)
person_6_2 = Frame(list_frame_2)
person_7_2 = Frame(list_frame_2)

list_2 = [person_1_2, person_2_2, person_3_2, person_4_2, person_5_2, person_6_2, person_7_2]

for index in range(class_size.get()):
    next_person_2 = list_2[index]
    next_person_2.pack(side=TOP, fill=X)
    Label(next_person_2, textvariable=display_names_2[index], font=general_font, fg='#3066be').pack(side=LEFT)
    Label(next_person_2, width=5).pack(side=LEFT)
    Label(next_person_2, textvariable=display_dates_2[index], font=general_font, fg='#009973').pack(side=RIGHT)
    
# -------------------------------------------------------------------------------------------------

Label(window, width=3).pack(side=LEFT)

file_computer_names = []
file_computer_dates = []

name1_3 = StringVar()
name2_3 = StringVar()
name3_3 = StringVar()
name4_3 = StringVar()
name5_3 = StringVar()
name6_3 = StringVar()
name7_3 = StringVar()

date1_3 = StringVar()
date2_3 = StringVar()
date3_3 = StringVar()
date4_3 = StringVar()
date5_3 = StringVar()
date6_3 = StringVar()
date7_3 = StringVar()

display_names_3 = [name1_3, name2_3, name3_3, name4_3, name5_3, name6_3, name7_3]
display_dates_3 = [date1_3, date2_3, date3_3, date4_3, date5_3, date6_3, date7_3]

list_frame_3 = Frame(window)
list_frame_3.pack(side=LEFT)

Label(list_frame_3, text='Computer', font=title_font, fg='#f46036', pady=5, padx=5, width=18, bg='#f9f1d2').pack(side=TOP)

person_1_3 = Frame(list_frame_3)
person_2_3 = Frame(list_frame_3)
person_3_3 = Frame(list_frame_3)
person_4_3 = Frame(list_frame_3)
person_5_3 = Frame(list_frame_3)
person_6_3 = Frame(list_frame_3)
person_7_3 = Frame(list_frame_3)

list_3 = [person_1_3, person_2_3, person_3_3, person_4_3, person_5_3, person_6_3, person_7_3]

for index in range(class_size.get()):
    next_person_3 = list_3[index]
    next_person_3.pack(side=TOP, fill=X)
    Label(next_person_3, textvariable=display_names_3[index], font=general_font, fg='#3066be').pack(side=LEFT)
    Label(next_person_3, width=5).pack(side=LEFT)
    Label(next_person_3, textvariable=display_dates_3[index], font=general_font, fg='#009973').pack(side=RIGHT)
    
# -------------------------------------------------------------------------------------------------

Label(window, width=3).pack(side=LEFT)

file_whiteboard_names = []
file_whiteboard_dates = []

name1_4 = StringVar()
name2_4 = StringVar()
name3_4 = StringVar()
name4_4 = StringVar()
name5_4 = StringVar()
name6_4 = StringVar()
name7_4 = StringVar()

date1_4 = StringVar()
date2_4 = StringVar()
date3_4 = StringVar()
date4_4 = StringVar()
date5_4 = StringVar()
date6_4 = StringVar()
date7_4 = StringVar()

display_names_4 = [name1_4, name2_4, name3_4, name4_4, name5_4, name6_4, name7_4]
display_dates_4 = [date1_4, date2_4, date3_4, date4_4, date5_4, date6_4, date7_4]

list_frame_4 = Frame(window)
list_frame_4.pack(side=LEFT)

Label(list_frame_4, text='Whiteboard', font=title_font, fg='#f46036', pady=5, padx=5, width=18, bg='#f9f1d2').pack(side=TOP)

person_1_4 = Frame(list_frame_4)
person_2_4 = Frame(list_frame_4)
person_3_4 = Frame(list_frame_4)
person_4_4 = Frame(list_frame_4)
person_5_4 = Frame(list_frame_4)
person_6_4 = Frame(list_frame_4)
person_7_4 = Frame(list_frame_4)

list_4 = [person_1_4, person_2_4, person_3_4, person_4_4, person_5_4, person_6_4, person_7_4]

for index in range(class_size.get()):
    next_person_4 = list_4[index]
    next_person_4.pack(side=TOP, fill=X)
    Label(next_person_4, textvariable=display_names_4[index], font=general_font, fg='#3066be').pack(side=LEFT)
    Label(next_person_4, width=5).pack(side=LEFT)
    Label(next_person_4, textvariable=display_dates_4[index], font=general_font, fg='#009973').pack(side=RIGHT)
    
# -------------------------------------------------------------------------------------------------

load_list('list', class_ref + '.txt', display_names_1, display_dates_1, file_list_names, file_list_dates)
load_list('jasper', class_ref + '.txt', display_names_2, display_dates_2, file_jasper_names, file_jasper_dates)
load_list('computer', class_ref + '.txt', display_names_3, display_dates_3, file_computer_names, file_computer_dates)
load_list('whiteboard', class_ref + '.txt', display_names_4, display_dates_4, file_whiteboard_names, file_whiteboard_dates)

print_lists()

window.mainloop()

os.system("cls" if os.name == "nt" else "clear")
