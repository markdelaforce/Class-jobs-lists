from tkinter import *
from tkinter import font
import datetime
import os

LargeButtonBack = '#635380'
smallButtonBack = '#a5668b'
buttonText = '#fff480'
labelColour = '#fcf8e8'
labelText = '#49919c'

def display_class_lists(event=None, class_index=0):
    
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'Not Done']

    def load_list(directory, filename, display_names, display_dates, text_file_names, text_file_dates):
        os.chdir('../job lists/' + directory)
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
            if (date_elements[1] == '13'):
                date = months[int(date_elements[1])-1]
            else:
                date = date_elements[2] + ' ' + months[int(date_elements[1])-1]
            display_dates[index].set(date)
        os.chdir('../../jobs')
        
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
    
    def choose_next_person(event=None, update_status='', next_name='', file_names=[], file_dates=[], _index=0, display_names=[], display_dates=[], folder='', filename=''):
        if not updating_list():
            update_status.set('update')
            for index in range(4):
                if updateStatuses[index].get() == 'update':
                    select_buttons_text[index].set('select')
                else:
                    select_buttons_text[index].set('')
            next_name.set(file_names[0])
        elif update_status.get() == 'update':
            next_name.set('')
            file_names.append(file_names.pop(_index.get()))
            file_dates.pop(_index.get())
            file_dates.append(str(datetime.datetime.now()).split()[0])
            for index in range(len(file_names)):
                display_names[index].set(file_names[index])
                date_elements = file_dates[index].split('-')
                set_date_display(date_elements, display_dates, index)
            _index.set(0)
            os.chdir('../job lists/' + folder)         
            names_file = open(filename, 'w')
            for index in range(len(file_names)):
                names_file.write(str(file_names[index]) + ',' + str(file_dates[index]) + '\n')
            names_file.close()
            os.chdir('../../jobs')
            update_status.set('initial')
            for index in range(4):
                select_buttons_text[index].set('choose next')
        
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
            
    def set_date_display(date_elements, display_dates, index):
        if (date_elements[1] == '13'):
            display_dates[index].set(months[int(date_elements[1])-1])
        else:
            display_dates[index].set(date_elements[2] + ' ' + months[int(date_elements[1])-1])
    
    def reset_list(event=None, original_names=[], changed_names=[], original_dates=[], changed_dates=[], folder='', filename='', display_names=[], display_dates=[]):
        if not updating_list():            
            for index in range(len(original_names)):
                display_names[index].set(original_names[index])
                date_elements = original_dates[index].split('-')
                set_date_display(date_elements, display_dates, index)
            os.chdir('../job lists/' + folder)         
            names_file = open(filename, 'w')
            for index in range(len(original_names)):
                names_file.write(str(original_names[index]) + ',' + str(original_dates[index]) + '\n')
                changed_names[index] = original_names[index]
                changed_dates[index] = original_dates[index]
            names_file.close()
            os.chdir('../../jobs')
            
    def duplicate(list_to_duplicate):
        new_list = []
        for item in range(len(list_to_duplicate)):
            new_list.append(list_to_duplicate[item])
        return new_list
    
    def print_lists():
        file_names = ['names list', 'jasper', 'computer', 'whiteboard']
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
        print('------------------------------\n------------------------------\n')
        
    def undoButton(index):
        button = Label(undo_buttons, text='Undo', bg=smallButtonBack, fg=buttonText, font=general_font, width=7, bd=4, relief='raised')
        button.pack(side=LEFT)  
        button.bind("<Button-1>", lambda event: reset_list(event,
        original_names=restoreNames[index],
        changed_names=fileNames[index],
        original_dates=restoreDates[index],
        changed_dates=fileDates[index],
        folder=folders[index],
        filename=group + '.txt',
        display_names=displayNames[index],
        display_dates=displayDates[index]))
        return button
        
    def selectButton(index):
        button = Label(buttons, textvariable=select_buttons_text[index], font=general_font, bg=LargeButtonBack, fg=buttonText, width=12, bd=4, relief='raised')
        button.pack(side=LEFT)
        button.bind("<Button-1>", lambda event: choose_next_person(event,
        update_status=updateStatuses[index],
        next_name=nextNames[index],
        file_names=fileNames[index],
        file_dates=fileDates[index],
        _index=_indexes[index],
        display_names=displayNames[index],
        display_dates=displayDates[index],
        folder=folders[index],
        filename=group + '.txt'))
        return button
        
    def name_display(padding):
        display = Label(next_name_display, textvariable=list_next_name, width=12, font=general_font, pady=10, fg='#f0386b', bd=4, relief='flat').pack(side=LEFT)
        if padding == 'padding':
            Label(buttons, width=23).pack(side=LEFT)
            Label(next_name_display, width=23).pack(side=LEFT)
        return display
        
    def list_holder(text):
        holder = Frame(window)
        holder.pack(side=LEFT)
        Label(holder, text=text, font=title_font, fg=labelText, pady=5, padx=5, width=18, bg=labelColour).pack(side=TOP)
        return holder
        
    def createEntry(display_names, display_dates, list_holder, _list):
        name = StringVar()
        display_names.append(name)
        date = StringVar()
        display_dates.append(date)
        person = Frame(list_holder)
        _list.append(person)
        person.pack(side=TOP, fill=X)
        Label(person, textvariable=display_names[i], font=general_font, fg='#3066be').pack(side=LEFT)
        Label(person, width=5).pack(side=LEFT)
        Label(person, textvariable=display_dates[i], font=general_font, fg='#009973').pack(side=RIGHT)
        
    window = Toplevel()
    window.title("Class jobs")
    window.geometry('1440x800+0+0')
    window.resizable(width=FALSE, height=FALSE)
    
    header_font = font.Font(family='comic sans ms', size=60, weight='bold')
    title_font = font.Font(family='comic sans ms', size=28, weight='bold')
    general_font = font.Font(family='comic sans ms', size=22, weight='bold')

    classes = ['mon 4.15', 'mon 5.30', 'tues 4.00', 'tues 5.15', 'weds 5.00', 'weds 6.15', 'thurs 5.30', 'thurs 6.30', 'fri 4.15']
    class_sizes = [2, 3, 3, 4, 3, 5, 4, 3, 7]
    class_size = IntVar()
    class_size.set(class_sizes[class_index])
    group = classes[class_index]

    header = Label(window, text="Class Jobs", bg=smallButtonBack, fg='#97c7ce', width='40', height='2', font=header_font).pack()
    Label(window, height=7).pack()
    
    Label(window, height=2).pack(side=BOTTOM)
    undo_buttons = Frame(window)
    undo_buttons.pack(side=BOTTOM)
    
    undo_button_1 = undoButton(0)
    Label(undo_buttons, width=31).pack(side=LEFT)
    undo_button_2 = undoButton(1)
    Label(undo_buttons, width=31).pack(side=LEFT)
    undo_button_3 = undoButton(2)
    Label(undo_buttons, width=31).pack(side=LEFT)    
    undo_button_4 = undoButton(3)

    footer_frame = Frame(window)
    footer_frame.pack(side=BOTTOM)
    buttons = Frame(footer_frame)
    buttons.pack()
    next_name_display = Frame(footer_frame)
    next_name_display.pack()
    
    select_buttons_text = []
    for i in range(4):
        button_text = StringVar()
        button_text.set('choose next')
        select_buttons_text.append(button_text)
    
    list_update_status = StringVar()
    jasper_update_status = StringVar()
    computer_update_status = StringVar()
    whiteboard_update_status = StringVar()
    updateStatuses = [list_update_status, jasper_update_status, computer_update_status, whiteboard_update_status]
    for status in updateStatuses:
        status.set('initial')
        
    list_next_name = StringVar()
    jasper_next_name = StringVar()
    computer_next_name = StringVar()
    whiteboard_next_name = StringVar()
    nextNames = [list_next_name, jasper_next_name, computer_next_name, whiteboard_next_name]
    
    list_index = IntVar()
    jasper_index = IntVar()
    computer_index = IntVar()
    whiteboard_index = IntVar()
    _indexes = [list_index, jasper_index, computer_index, whiteboard_index]
    for index in _indexes:
        index.set(0)
        
    list_button = selectButton(0)
    list_next_display = name_display('padding')

    jasper_button = selectButton(1)
    jasper_next_display = name_display('padding')

    computer_button = selectButton(2)
    computer_next_display = name_display('padding')

    whiteboard_button = selectButton(3)
    whiteboard_next_display = name_display('no-padding')

    window.bind("<Down>", next_name)
    window.bind("<Up>", last_name)
    
    # -------------------------------------------------------------------------------------------------

    Label(window, width=3).pack(side=LEFT)
    list_holder_1 = list_holder('Names List')
    
    display_names_1 = []
    display_dates_1 = []
    list_1 = []
    
    for i in range(class_size.get()):
        createEntry(display_names_1, display_dates_1, list_holder_1, list_1)
        
    Label(list_holder_1, height=2).pack()
    
    # -------------------------------------------------------------------------------------------------

    Label(window, width=3).pack(side=LEFT)    
    list_holder_2 = list_holder('Jasper')

    display_names_2 = []
    display_dates_2 = []
    list_2 = []

    for i in range(class_size.get()):
        createEntry(display_names_2, display_dates_2, list_holder_2, list_2)
    
    Label(list_holder_2, height=2).pack()
    
    # -------------------------------------------------------------------------------------------------

    Label(window, width=3).pack(side=LEFT)
    list_holder_3 = list_holder('Computer')
    
    display_names_3 = []
    display_dates_3 = []
    list_3 = []
    
    for i in range(class_size.get()):
        createEntry(display_names_3, display_dates_3, list_holder_3, list_3)
    
    Label(list_holder_3, height=2).pack()
    
    # -------------------------------------------------------------------------------------------------

    Label(window, width=3).pack(side=LEFT)
    list_holder_4 = list_holder('Whiteboard')
    
    display_names_4 = []
    display_dates_4 = []
    list_4 = []

    for i in range(class_size.get()):
        createEntry(display_names_4, display_dates_4, list_holder_4, list_4)
    
    Label(list_holder_4, height=2).pack()
    
    # -------------------------------------------------------------------------------------------------
    
    file_list_names = []
    file_list_dates = []
    file_jasper_names = []
    file_jasper_dates = []
    file_computer_names = []
    file_computer_dates = []
    file_whiteboard_names = []
    file_whiteboard_dates = []

    load_list('list', group + '.txt', display_names_1, display_dates_1, file_list_names, file_list_dates)
    load_list('jasper', group + '.txt', display_names_2, display_dates_2, file_jasper_names, file_jasper_dates)
    load_list('computer', group + '.txt', display_names_3, display_dates_3, file_computer_names, file_computer_dates)
    load_list('whiteboard', group + '.txt', display_names_4, display_dates_4, file_whiteboard_names, file_whiteboard_dates)
    
    restore_list_names = duplicate(file_list_names)
    restore_list_dates = duplicate(file_list_dates)
    restore_jasper_names = duplicate(file_jasper_names)
    restore_jasper_dates = duplicate(file_jasper_dates)
    restore_computer_names = duplicate(file_computer_names)
    restore_computer_dates = duplicate(file_computer_dates)
    restore_whiteboard_names = duplicate(file_whiteboard_names)
    restore_whiteboard_dates = duplicate(file_whiteboard_dates)
    
    restoreNames =  [restore_list_names, restore_jasper_names, restore_computer_names, restore_whiteboard_names]
    fileNames =     [file_list_names,    file_jasper_names,    file_computer_names,    file_whiteboard_names]
    restoreDates =  [restore_list_dates, restore_jasper_dates, restore_computer_dates, restore_whiteboard_dates]
    fileDates =     [file_list_dates,    file_jasper_dates,    file_computer_dates,    file_whiteboard_dates]
    folders =       ['list',             'jasper',             'computer',             'whiteboard']
    displayNames =  [display_names_1,    display_names_2,      display_names_3,        display_names_4]
    displayDates =  [display_dates_1,    display_dates_2,      display_dates_3,        display_dates_4]
    
    print_lists()
    