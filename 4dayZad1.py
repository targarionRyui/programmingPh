# 1 Задание

# import csv
#
# with open("59778.csv", "r") as f:
#     n = csv.reader(f, delimiter=';')
#     count = 0
#     l = []
#     for row in n:
#         numbers = [int(x) for x in row]
#         l.append(numbers)
#
#     for i in range(len(l)):
#         l[i].sort()
#         pov = [int(x) for x in l[i] if l[i].count(x) == 4]
#         nepov = [int(x) for x in l[i] if l[i].count(x) == 1]
#         if len(pov) == 4 and len(nepov) == 3 and pov[0] > sum(nepov)/3:
#             count += 1
#     print(count)



# 2 Задание

import csv

with open("29666.csv", "r") as f:
    l = []
    for i in f:
        l.append(float(i.replace(",", ".")))

    spOr = []

    while True:
        sp = []
        while True:
            if len(l) == 2:
                break
            elif l[0] > l[1]:
                sp.append(l[0])
                l.pop(0)
            else:
                l.pop(0)
                break
        if len(sp) > 1:
            spOr.append(sp)
        if len(l) == 2:
            break

    sumMax = 0.0
    spPok = []
    for i in range(len(spOr)):
        sumSp = sum(spOr[i])
        if sumMax < sumSp:
            sumMax = sumSp
            spPok = spOr[i]
    print(spOr)
    print(sumMax) #319.36 это максимальная сумма, подряд идущих чисел по условию из всех других
    print(spPok) # Это список с макс суммой

