# Задание 1
# def vych(str,res,j):
#     list1 = list(str)
#
#     if list1[j] == '1':
#         res += 1
#     elif list1[j] == '2':
#         res += 2
#     elif list1[j] == '3':
#         res *= 2
#     else:
#         print("Invalid chtoly?")
#     j += 1
#     if j < len(list1):
#         return vych(str, res,j)
#     return res
#
#
# print(vych("132",7,0))
#
#
# def skilk(start, end):
#
#     count1 = 0
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         count1 += skilk(start+1, end)
#         count1 += skilk(start+2, end)
#         count1 += skilk(start*2, end)
#
#
#     return count1
#
#
# prom = skilk(3,10)
# ending = skilk(10,12)
# print(prom)
# print(ending)
# print("Все пути от 3 до 12 проходящие через 10 = ", prom * ending)






# Задание 2
# def vych(str,res,j):
#     list1 = list(str)
#     maxkol = len(str)
#
#     if list1[j] == '1':
#         res += 1
#     elif list1[j] == '2':
#         res = res * 2 + 1
#     else:
#         print("Invalid chtoly?")
#     j += 1
#     if j < len(list1):
#         return vych(str, res,j)
#     return res
#
#
# print(vych("121",7,0))
# def skilk(start, end, prom):
#     s = []
#     count1 = 0
#     count2 = 0
#
#     if start == prom:
#         return 0
#     elif start == end:
#         return 1
#     elif start > end:
#         return 0
#     if start < end:
#         count1 += skilk(start+1, end, prom)
#         count1 += skilk(start*2+1, end, prom)
#
#     return count1
#
# print(skilk(1,27, 26))




# Задание 3
# def vych(str,res,j):
#     list1 = list(str)
#
#     if list1[j] == '1':
#         res += 1
#     elif list1[j] == '2':
#         res += 2
#     else:
#         print("Invalid chtoly?")
#     j += 1
#     if j < len(list1):
#         return vych(str, res,j)
#     return res
#
#
# print(vych("212",7,0))
#
# def skilk(start, end, prom):
#     count1 = 0
#
#     if start == prom:
#         return 0
#     elif start == end:
#         return 1
#     elif start > end:
#         return 0
#     if start < end:
#         count1 += skilk(start+1, end, prom)
#         count1 += skilk(start+2, end, prom)
#
#     return count1
#
#
# def skilk2(start, end):
#
#     count1 = 0
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         count1 += skilk2(start+1, end)
#         count1 += skilk2(start+2, end)
#         count1 += skilk2(start*2, end)
#
#
#     return count1
#
#
#
#
# prom = skilk2(2,9)
# ending = skilk(9,18, 14)
#
# print(prom)
# print(ending)
# print("Все пути от 2 до 18 проходящие через 9 и не проходящая через 14 = ", prom * ending)


