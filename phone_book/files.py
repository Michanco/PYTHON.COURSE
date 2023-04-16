with open('book.txt', 'w', encoding='utf-8') as f:
    f.write('фио |  номер телефона')

with open('book.txt', 'a', encoding='utf-8') as f:
    f.write('\nфио1 |  номер телефона1')

with open('book.txt', 'r', encoding='utf-8') as f:
    print(f.read())
