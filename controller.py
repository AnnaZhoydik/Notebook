import view, module


def start():
    view.welcome()
    path = "Notebook.txt"
    module.create(path)
    while True:
        choice = view.interface()
        if choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5' and choice != '6':
            view.error()
        elif choice == '1':
            name = input('Введите название заметки: ')
            text = input('Введите текст заметки: ')
            module.add_cont(name, text)
            view.ok()
        elif choice == '2':
            module.show_all()
        elif choice == '3':
            find = input('Введите название: ')
            module.search(find)
        elif choice == '4':
            fam = input('Введите текст для редактирования: ')
            module.change(path, fam)
        elif choice == '5':
            delete = input('Введите строку для удаления: ')
            module.delete_contact(path, delete)
        elif choice == '6':
            view.goodbye()
            break
