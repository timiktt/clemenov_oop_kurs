from tkinter import *
from tkinter import ttk, filedialog, messagebox


list_keys = [
    'last_name',
    'first_p_name',
    'number_phone',
    'address',
]

#==========================================
#ЗАПРОСЫ ______НАЧАЛО_______
#==========================================
actual_data = []
def get_data():
    data_to_convert = []
    actual_data.clear()
    for items in table_users.get_children():
        row = table_users.item(items)
        actual_data_str = ''
        for i in range(len(row['values'])):
            actual_data_str += str(row['values'][i])
            actual_data_str += ' '
        data_to_convert.append(actual_data_str)
    for i in range(len(data_to_convert)):
        obj_dict = {}
        obj_list = data_to_convert[i].split(' ')
        for i in range(len(list_keys)):
            obj_dict[list_keys[i]] = obj_list[i]
        actual_data.append(obj_dict)   

def get_number_with_l_name(l_name: str):
    get_data()
    info = ''
    for items in actual_data:
        if items['last_name'].lower() == l_name.lower():
            info += items['number_phone']
            info += '\n'
    if info == '':
        info += 'Инфомация о данном\nсотруднике отсутствует' 
    return info



#==========================================
#ФУНКЦИИ ФОРМЫ ______НАЧАЛО_______
#==========================================
def select_request():
    if var.get() == 1:
        child_form_req_1()
    elif var.get() == 2:
        child_form_req_2()
    elif var.get() == 3:
        child_form_req_3()
    elif var.get() == 4:
        child_form_req_4()
    else:
        print('Ошибка')

def check_emty_enty():
    if entry_last_name.get().replace(' ', '') == '':
        return False
    elif entry_first_p_name.get().replace(' ', '') == '':
        return False
    elif entry_phone_number.get().replace(' ', '') == '':
        return False
    elif entry_address.get().replace(' ', '') == '':
        return False
    else:
        return True
def add_data():
    data = []
    if check_emty_enty():
        data.append(str(entry_last_name.get()).replace(' ', ''))
        data.append(str(entry_first_p_name.get()).replace(' ', ''))
        data.append(str(entry_phone_number.get()).replace(' ',''))
        data.append(str(entry_address.get()).replace(' ', ''))
        table_users.insert("", END, values=data)
        entry_last_name.delete(0, END)
        entry_first_p_name.delete(0, END)
        entry_phone_number.delete(0, END)
        entry_address.delete(0, END)

def edit_data():
    def command_ok():
        if check_emty_enty():
            data = []
            data.append(str(entry_last_name.get()).replace(' ', ''))
            data.append(str(entry_first_p_name.get()).replace(' ', ''))
            data.append(str(entry_phone_number.get()).replace(' ',''))
            data.append(str(entry_address.get()).replace(' ', ''))
            table_users.item(table_users.selection(), value=data)
            entry_last_name.delete(0, END)
            entry_first_p_name.delete(0, END)
            entry_phone_number.delete(0, END)
            entry_address.delete(0, END)
            button_add.configure(text='Добавить', command=add_data, background='white')
            button_edit.configure(text='Изменить', command=edit_data, background='white')
    def command_cancel():
        button_add.configure(text='Добавить', command=add_data, background='white')
        button_edit.configure(text='Изменить', command=edit_data, background='white')
        entry_last_name.delete(0, END)
        entry_first_p_name.delete(0, END)
        entry_phone_number.delete(0, END)
        entry_address.delete(0, END)
    if table_users.selection():
        button_add.configure(text='Ок', command=command_ok, background='green')
        button_edit.configure(text='Отмена', command=command_cancel, background='red')
        entry_last_name.delete(0, END)
        entry_first_p_name.delete(0, END)
        entry_phone_number.delete(0, END)
        entry_address.delete(0, END)
        row = table_users.item(table_users.selection())
        entry_last_name.insert(0, row['values'][0])
        entry_first_p_name.insert(0, row['values'][1])
        entry_phone_number.insert(0, row['values'][2])
        entry_address.insert(0, row['values'][3])

def delete_select():
    if table_users.selection():
        table_users.delete(table_users.selection())

def delete_data_in_table():
    for item in table_users.get_children():
        table_users.delete(item)

#==========================================
#ОПИСАНИЕ ДОЧЕРНИХ ОКОН ______НАЧАЛО_______
#==========================================
def child_form_req_1():
    def configure_label():
        l_name = entry_intro.get()
        l_name = l_name.replace(' ', '')
        info = get_number_with_l_name(l_name)
        label_text.configure(text=info)
    window = Toplevel(main_window, background='gray', width=700, border=10, relief=SUNKEN)
    window.title('Найти телефон сотрудника по его фамилии')
    window.geometry('300x250')
    label_intro = Label(window, text='Введите фамилию сотрудника', background='gray', font=10)
    label_intro.grid(row=0, column=0)
    entry_intro = Entry(window, font=10)
    entry_intro.grid(row=1, column=0)
    button = Button(window,text='Найти', background='lightgray', font=10, relief=SUNKEN, width=20, command=configure_label)
    button.grid(row=2, column=0, pady=10)
    label_text = Label(window, text='', font=14, background='gray')
    label_text.grid(row=3, column=0, pady=10, padx=10)

def child_form_req_2():
    test_text = 'Хайретдинов ТС\nХайретдинов ТС\nХайретдинов ТС\nХайретдинов ТС\n Хайретдинов ТС\n Хайретдинов ТС'
    def configure_label():
        label_text.configure(text=test_text, background='lightgray')
    window = Toplevel(main_window, background='gray', width=700, border=10, relief=SUNKEN)
    window.title('Найти список сотрудников, чьи фамилии начинаются с заданных букв')
    window.geometry('330x250')
    label_intro = Label(window, text='Введите несколько первых букв фамилии', background='gray', font=10)
    label_intro.grid(row=0, column=0)
    entry_intro = Entry(window, font=10)
    entry_intro.grid(row=1, column=0)
    button = Button(window,text='Найти', background='lightgray', font=10, relief=SUNKEN, width=20, command=configure_label)
    button.grid(row=2, column=0, pady=10)
    label_text = Label(window, text='', font=14, background='gray')
    label_text.grid(row=3, column=0, pady=10, padx=10)

def child_form_req_3():
    test_text = '+79960023192\n+79960023192\n+79960023192\n+79960023192\n +79960023192\n+79960023192'
    def configure_label():
        label_text.configure(text=test_text, background='lightgray')
    window = Toplevel(main_window, background='gray', width=700, border=10, relief=SUNKEN)
    window.title('Найти список сотрудников, чьи телефоны начинаются с заданных цифр')
    window.geometry('330x250')
    label_intro = Label(window, text='Введите несколько первых цифр номера', background='gray', font=10)
    label_intro.grid(row=0, column=0)
    entry_intro = Entry(window, font=10)
    entry_intro.grid(row=1, column=0)
    button = Button(window,text='Найти', background='lightgray', font=10, relief=SUNKEN, width=20, command=configure_label)
    button.grid(row=2, column=0, pady=10)
    label_text = Label(window, text='', font=14, background='gray')
    label_text.grid(row=3, column=0, pady=10, padx=10)

def child_form_req_4():
    test_text = 'Богдановича2/27кв156\nБогдановича2/27кв156\nБогдановича2/27кв156\n+Богдановича2/27кв156\nБогдановича2/27кв156\n+79960023192'
    def configure_label():
        label_text.configure(text=test_text, background='lightgray')
    window = Toplevel(main_window, background='gray', width=700, border=10, relief=SUNKEN)
    window.title('Найти адрес сотрудника по номеру телефона')
    window.geometry('330x250')
    label_intro = Label(window, text='Введите номер телефона сотрудника', background='gray', font=10)
    label_intro.grid(row=0, column=0)
    entry_intro = Entry(window, font=10)
    entry_intro.grid(row=1, column=0)
    button = Button(window,text='Найти', background='lightgray', font=10, relief=SUNKEN, width=20, command=configure_label)
    button.grid(row=2, column=0, pady=10)
    label_text = Label(window, text='', font=14, background='gray')
    label_text.grid(row=3, column=0, pady=10, padx=10)

#==========================================
#ОПИСАНИЕ ГЛАВНОГО ОКНА ______НАЧАЛО_______
#==========================================

main_window = Tk()
main_window.geometry('1015x550')
main_window.title('База абонентов')

#Менб сверху программы 
#_______________________________________
menu = Menu(main_window)
main_window.config(menu=menu)
file = Menu(menu)
menu.add_cascade(label='Файл', menu=file)
name_and_comands = {
    'Открыть файл': 'command1', 
    'Сохранить файл': 'command2',
    'Закрыть файл': 'commad3',
}
for key, value in name_and_comands.items():
    file.add_command(label=key,)
#_______________________________________

#Создание таблицы 
#_______________________________________
table_columns = {
    'last_name': 'Фамилия',
    'first_p_name': 'Инициалы',
    'number_phone': 'Номер телефона',
    'address': 'Адрес',
}
columns = (
    'last_name',
    'first_p_name',
    'number_phone',
    'address',
)
table_users = ttk.Treeview(columns=columns, show='headings')
for key, value in table_columns.items():
    table_users.heading(f'{key}', text=f'{value}')
for i in range(len(columns)):
    table_users.column(f"#{i+1}", stretch=NO, width=210, anchor=N)
table_users.grid(row=0, column=0, padx=5)
#_______________________________________

#Создание поля добавить/изменить
#_______________________________________________
frame_place = Frame(main_window, background='gray', width=700, border=10, relief=SUNKEN)
#Фамилия 
label_last_name = Label(frame_place, text='Фамилия', padx=10, pady=10,  background='gray', font='10')
label_last_name.grid(row=0, column=0)
entry_last_name = Entry(frame_place, font='10')
entry_last_name.grid(row=1, column=0, padx=10)
#Инициалы
label_first_p_name = Label(frame_place, text='Инициалы', padx=10, pady=10,  background='gray', font='10')
label_first_p_name.grid(row = 0, column=1)
entry_first_p_name = Entry(frame_place, font='10')
entry_first_p_name.grid(row=1,column=1, padx=10)
#Номер телефона
label_phone_number = Label(frame_place, text='Номер Телефона', padx=10, pady=10,  background='gray', font='10')
label_phone_number.grid(row = 0, column=2)
entry_phone_number = Entry(frame_place, font='10')
entry_phone_number.grid(row=1,column=2, padx=10)
#Адрес
label_address = Label(frame_place, text='Адрес', padx=10, pady=10,  background='gray', font='10')
label_address.grid(row = 0, column=3)
entry_address = Entry(frame_place, font='10')
entry_address.grid(row=1,column=3, padx=10)
#Кнопка добавить
button_add = Button(frame_place, text='Добавить', width=15, command=add_data)
button_add.grid(row=0, column=4, padx=20)
#Кнопка изменить
button_edit = Button(frame_place, text='Изменить', width=15, command=edit_data)
button_edit.grid(row=1, column=4, padx=20)
frame_place.grid(row=1, column=0, padx=10, pady=10)

#КНОПКИ УДАЛИТЬ
frame_button_del = Frame(main_window, background='gray', width=700, border=10, relief=SUNKEN, padx=10, pady=10)
buttod_del_row = Button(frame_button_del, text='Удалить строчку', font=10, width=15, padx=5, pady=5, command=delete_select)
buttod_del_row.grid(row=0, column=0, padx=10)
buttod_del_all = Button(frame_button_del, text='Удалить все данные', font=10, width=15, padx=20, pady=5, command=delete_data_in_table)
buttod_del_all.grid(row=0, column=1, padx=10)
frame_button_del.grid(row=2, column=0)
#_______________________________________________
#Создание поля запросов
frame_requests = Frame(main_window, background='gray', width=1000, border=10, relief=SUNKEN)
label_request_1 = Label(frame_requests, text='Найти телефон сотрудника по его фамилии', background='gray', font='10')
label_request_2 = Label(frame_requests, text='Найти список сотрудников, чьи фамилии начинаются с заданных букв', background='gray', font='10')
label_request_3 = Label(frame_requests, text='Найти список сотрудников, чьи телефоны начинаются с заданных цифр', background='gray', font='10')
label_request_4 = Label(frame_requests, text='Найти адрес сотрудника по номеру телефона', background='gray', font='10')
label_request_1.grid(row=0, column=0)
label_request_2.grid(row=1, column=0)
label_request_3.grid(row=2, column=0)
label_request_4.grid(row=3, column=0)
frame_requests.place(x=100, y=420)

var = IntVar()
var.set(None)

rb_request_1 = Radiobutton(frame_requests, variable=var, value=1, background='gray')
rb_request_2 = Radiobutton(frame_requests, variable=var, value=2, background='gray')
rb_request_3 = Radiobutton(frame_requests, variable=var, value=3, background='gray')
rb_request_4 = Radiobutton(frame_requests, variable=var, value=4, background='gray')
rb_request_1.grid(row=0, column=1)
rb_request_2.grid(row=1, column=1)
rb_request_3.grid(row=2, column=1)
rb_request_4.grid(row=3, column=1)

button_view_request = Button(main_window, text='Выполнить запрос', width=20, height=5, font=10, relief=SUNKEN, background='gray', command=select_request)
button_view_request.place(x=680, y=430)
main_window.mainloop()