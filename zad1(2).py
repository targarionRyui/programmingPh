
'''

            Онлайн компилятор Python с интерфейсом на русском языке.
       Вставьте код в IDE, скомпилируйте и запустите программу на python онлайн.
      Напишите свой код в редакторе и нажмите кнопку "Выполнить", чтобы проверить его.
                 Бесплатный интерпретатор кода прямо в браузере.

'''
1
Задание 1
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())


if not (1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8):
    print("Ошибка!")
else:
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
        print("Пойдет")
    else:
        print("Не пойдет")
        
Задание 2 
k = int(input())
n = int(input())

sum = 0
for i in range(k,n+1):
    if i % 2 == 0:
        sum += i
print(sum)

Задание 3
a = int(input())
sum = 0
while(a != 0):
    sum += a
    a = int(input())
print(sum)

Задание 4
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(fact)