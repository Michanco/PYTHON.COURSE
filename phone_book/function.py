def show_data() -> None:
    '''Выводит информацию из справочника'''
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read())

def add_data() -> None:
    '''Добавляет иформацию в справочник'''
    fio = input(('Введите ФИО:  '))
    tel_number = input('Введите номер телефона:  ')
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{fio} |  {tel_number}')

def find_data() -> None:
    '''Осуществляет поиск по справочнику'''
    print('Введите данные для поиска  ')
    data = input()
    with open('book.txt', 'w+', encoding='utf-8') as f:
        tel_book = f.read()
    print(search(tel_book, data))

def search(book: str, info: str) -> str:
    '''Находит в строке записи по определённому кретерию поиска'''
    info = info.lower()
    book = book.split('\n')
    return [post for post in book if info in post.lower()]

def delete_data() -> None:
    '''Удаляет найденную запись, при наличие вариантов предлагает выбрать какую запись удалять'''
    print ('Введите данные для поиска строки')
    data = input().lower()
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
        tel_book = tel_book.split('\n')
        posts = [post for post in tel_book if data in post.lower()]
        index_del = [i for i in range(len(tel_book)) if data in tel_book[i].lower()]
    if len(posts) == 1:
        while True:
            print(f'Найдена одна запись. Подтвердите удаление нажмите "1". Для отмены нажмите "0" : \n{posts[0]} ')
            del1 = int(input())
            if del1 == 1:
                tel_book.pop(index_del[0])
                with open('book.txt', 'w', encoding='utf-8') as f:
                    for el in tel_book:
                        f.write(f'{el} \n')
                print('Запись успешно удалена')
                break
            elif del1 == 0:
                print('Удаление отменено')
                break
            else:
                break
    elif len(posts) == 0:
        print('Нет записей удовлетворяющих критериям поиска ')
    else:
        print('Найдено несколько записей:   ')
        for i in range(len(posts)):
            print(f'{i + 1} - {posts[i]}')
        while True:
            print('Выберите номер записи которую необходимо удалить. Для отмены нажмите "0"')
            del_2 = int(input())
            if del_2 == 0:
                print('Удаление отменено')
                break
            elif 0 < del_2 <= len(posts):
                tel_book.pop(index_del[del_2 - 1])
                with open('book.txt', 'w', encoding='utf-8') as f:
                    for el in tel_book:
                        f.write(f'{el} \n')
                print('Запись успешно удалена')
                break
            else:
                break

def change_data() -> None:
    '''Изменяет найденную запись, при наличие вариантов предлагает выбрать какую запись изменять'''
    print('Введите данные для поиска строки')
    data = input().lower()
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
        tel_book = tel_book.split('\n')
        posts = [post for post in tel_book if data in post.lower()]
        index_del = [i for i in range(len(tel_book)) if data in tel_book[i].lower()]
    if len(posts) == 1:
        while True:
            print(f'Найдена одна запись. Изменение ФИО нажмите "1". Изменение телефона нажмите "2". Для отмены нажмите "0" : \n{posts[0]} ')
            del1 = int(input())
            posts[0] = posts[0].split(' |  ')
            if del1 == 1:
                posts[0][0] = input('Введите новые ФИО: ')
                posts[0] = str(f'{posts[0][0]} |  {posts[0][1]}')
                tel_book[index_del[0]] = posts[0]
                with open('book.txt', 'w', encoding='utf-8') as f:
                    for el in tel_book:
                        f.write(f'{el} \n')
                print('ФИО успешно изменены')
                break
            elif del1 == 2:
                posts[0][1] = input('Введите новый телефон: ')
                posts[0] = str(f'{posts[0][0]} |  {posts[0][1]}')
                tel_book[index_del[0]] = posts[0]
                with open('book.txt', 'w', encoding='utf-8') as f:
                    for el in tel_book:
                        f.write(f'{el} \n')
                print('Телефон успешно изменён')
                break
            elif del1 == 0:
                print('Изменение отменено')
                break
            else:
                break
    elif len(posts) == 0:
        print('Нет записей удовлетворяющих критериям поиска ')
    else:
        print('Найдено несколько записей:   ')
        for i in range(len(posts)):
            print(f'{i + 1} - {posts[i]}')
        while True:
            print('Выберите номер записи которую необходимо изменить. Для отмены нажмите "0"')
            del2 = int(input())
            if del2 == 0:
                print('Изменение отменено')
                break
            elif 0 < del2 <= len(posts):
                posts[del2 - 1] = posts[del2 - 1].split(' |  ')
                while True:
                    print('Изменение ФИО нажмите "1". Изменение телефона нажмите "2". Для отмены нажмите "0"')
                    del3 = int(input())
                    if del3 == 1:
                        posts[del2 - 1][0] = input('Введите новые ФИО: ')
                        posts[del2 - 1] = str(f'{posts[del2 - 1][0]} |  {posts[del2 - 1][1]}')
                        tel_book[index_del[del2 - 1]] = posts[del2 - 1]
                        with open('book.txt', 'w', encoding='utf-8') as f:
                            for el in tel_book:
                                f.write(f'{el} \n')
                        print('ФИО успешно изменены')
                        break
                    elif del3 == 2:
                        posts[del2 - 1][1] = input('Введите новый телефон: ')
                        posts[del2 - 1] = str(f'{posts[del2 - 1][0]} |  {posts[del2 - 1][1]}')
                        tel_book[index_del[del2 - 1]] = posts[del2 - 1]
                        with open('book.txt', 'w', encoding='utf-8') as f:
                            for el in tel_book:
                                f.write(f'{el} \n')
                        print('Телефон успешно изменён')
                        break
                    elif del3 == 0:
                        print('Изменение отменено')
                        break
                    else:
                        break
                    tel_book[index_del[del2 - 1]] = posts[0]
                    with open('book.txt', 'w', encoding='utf-8') as f:
                        for el in tel_book:
                            f.write(f'{el} \n')
                break
            else:
                break



