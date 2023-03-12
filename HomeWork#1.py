# Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

a = input("Введите трёхзначное число: ")
if len(a) == 3:
    print(f" {a} -> {int(a[0])+ int(a[1]) + int(a[2]) } ({a[0]} + {a[1]} + {a[2]})")
else:
    print("!Input FATAL ERROR!")

# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

a = int(input(" Введите общее количество журавликов : "))
if a % 6 == 0:
    print(f"{a} -> {a//6}  {a//6*4}  {a//6}")
else:
    print("При таком количестве решение невозможно ")
 
# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

ticket = input("Введите шестизначный номер билета: ")
if len(ticket) == 6:
    if int(ticket[0]) + int(ticket[1]) + int(ticket[2]) == int(ticket[3]) + int(ticket[4]) + int(ticket[5]):
        print(f" {ticket} -> YES")
    else:
        print(f" {ticket} -> NO")
else:
    print("!Input FATAL ERROR!")


# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

print(" Введите размер шоколадки : ")
n = int(input())
print("на")
m = int(input())
k = int(input(" Сколько долек нужно отломить?  "))
if n*m > k:
    if k < n and k < m:
        print(" Не получится ")
    else:
        if k % n == 0 or k % m == 0:
            print(" Получится")
        else:
            print(" Не получится ")
elif n*m == k:
    print("Забирайте всю шоколадку")
else:
    print("Вы хотите отломить больше чем долек в шоколадке")