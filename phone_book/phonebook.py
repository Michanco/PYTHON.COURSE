import function

while True:
    print('1. вывод, 2. добавление, 3. поиск, 4. удаление, 5. изменение')
    mode = int(input())
    if mode == 1:
        function.show_data()
    elif mode == 2:
        function.add_data()
    elif mode == 3:
        function.find_data()
    elif mode == 4:
        function.delete_data()
    elif mode == 5:
        function.change_data()
    else:
        break



