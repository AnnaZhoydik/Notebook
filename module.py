import view
from datetime import datetime
import uuid


def add_cont(new_name, text):
    data = open('Notebook.txt', 'a')
    id = str(uuid.uuid4())
    date = datetime.now().strftime('%d.%m.%Y %H:%M')
    data.write("(" + id + ") " + "|" + new_name + "| " + text + " " + "[" + date + "]")
    data.close()


def show_all():
    data = open('Notebook.txt', "r")
    for line in data:
        print(line[:-1])
    data.close()


def search(stroka):
    a = 0
    data = open('Notebook.txt', 'r')
    for line in data:
        if stroka in line:
            print(line)
            a = 123
            break
    if a != 123:
        view.notfound()
    data.close()


def change(file_name, old_value):
    with open(file_name, "r+") as data1:
        contents = data1.read()
        if old_value in contents:
            new_value = input('Введите новое значение: ')
            contents = contents.replace(old_value, new_value)
            with open(file_name, "w") as data2:
                data2.write(contents)
            view.ok()
        else:
            view.notfound()


def delete_contact(file_name, old_value):
    with open(file_name, "r+") as data1:
        contents = data1.read().splitlines()
        a = 0
        for line in contents:
            if old_value in line:
                a = 123
                contents.remove(line)
                with open(file_name, "w") as data2:
                    for i in contents:
                        data2.write(i)
                        data2.write('\n')
                view.ok()
        if a != 123:
            view.notfound()


def create(base):
    try:
        file = open(base, 'r')
    except IOError:
        print('Создана новая книга заметок  -> Notebook.txt ')
        file = open(base, 'w')
    finally:
        file.close()
