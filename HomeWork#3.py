# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X. 
# Попробуйте использовать метод count(), а также решите задачу с помощью своего алгоритма (без count). 
# Замерьте время работы двух алгоритмов и сравните, подумайте, почему оно отличается.

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

elements = int(input('Введите количество элементов последовательности  '))
import random
import time

some_list = [random.randint(1, 10) for _ in range(elements)]
print(some_list)
count = 0
number = int(input('Введите число которое будем искать  '))

start = time.perf_counter()
for i in range(elements):
    if some_list[i] == number:
        count += 1
print(f' Число {number} встречается {count} раз')
end = time.perf_counter()
first_time = end - start

start = time.perf_counter()
count2 = some_list.count(number)
print(f' Число {number} встречается {count2} раз')
end = time.perf_counter()
second_time = end - start

print(first_time / second_time)

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

elements = int(input('Введите количество элементов последовательности  '))
import random
import time

some_list = [random.randint(1, 10) for _ in range(elements)]
print(some_list)
number = float(input('Введите число  с которым будем сравнивать  '))
difference = abs(number - some_list[0])
near_number = some_list[0]
near_number2 = False

for i in range(len(some_list)):
    if abs(number - some_list[i]) < difference:
        difference = abs(number - some_list[i])
        near_number = some_list[i]
    elif abs(number - some_list[i]) == difference and some_list[i] != near_number:
        near_number2 = some_list[i]
if near_number2 == False:
    print(f'Элемент последовательности самый близкий по величине к {number}  ->   {near_number}')
else:
    print(f'Элементы последовательности равнозначно близкие по величине к {number}  ->   {near_number} и {near_number2}')


# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; 
#     B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; 
#     Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

language = int(input('Выберите язык ( 1 = Русский, 2 = Английский)  '))
word = input('Введите слово ')
english = ((1,'a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r'),(2, 'd','g'), (3, 'b', 'c', 'm', 'p'), (4, 'f', 'h','v', 'w','y'), (5, 'k'), (8, 'j', 'x'), (10, 'q', 'z'))
russian = ((1, 'а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'), (2, 'д', 'к', 'л','м', 'п', 'у'), (3, 'б', 'г', 'ё', 'ь', 'я'), (4, 'й', 'ы'), 
           (5, 'ж', 'з', 'х', 'ц', 'ч'), (8, 'ш', 'э','ю'), (10, 'ф', 'щ', 'ъ'))
word_price = 0
if language == 1:
    for i in range(len(word)):
        for j in range(len(russian)):
            for k in range(1, len(russian[j])):
                if russian[j][k] == word[i]:
                    word_price += int(russian[j][0])
                    break
elif language == 2:
    for i in range(len(word)):
        for j in range(len(english)):
            for k in range(1, len(english[j])):
                if english[j][k] == word[i]:
                    word_price += int(english[j][0])
                    break
print(word)
print(word_price)