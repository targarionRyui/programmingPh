# def fun(sp):
#     l = []
#     if len(sp) > 2:
#         for q in range(len(sp)):
#             if sp[q] == 1:
#                 l.append(sp[q])  # dobav1
#                 continue
#             zas = sp[q] - l[q - 1]  # 7 - 1 = 6
#             # .     21         6     =   15
#             #      35         15.    =.  20
#             l.append(zas)  # dobav6 : 1,6
#             # dobav 15: 1,6,15, 20
#             if zas == 1:
#                 break
#         print(l)
#         return fun(l)
#     return [1]
#
#
# spis = [1, 7, 21, 35, 35, 21, 7, 1]
# print(fun(spis))


# 1
# def fact(n):
#     sum = 0
#     if n>=1:
#         return n  * fact(n-1)
#     return 1
# print(fact(6))
# # 2
# def n(str):
#     a = "aeiou"
#     b = list(str)
#     c = list(a)
#     h = []
#     for i in b:
#         if not i in c:
#             h.append(i)
#     j = ''.join(h)
#     return j
#
# print(n("sdafajweoipjfiowjw"))



# 3


# def fun(sp):
#     l = []
#     if len(sp) > 2:
#         for q in range(len(sp)):
#             if sp[q] == 1:
#                 l.append(sp[q])  # dobav1
#                 continue
#             zas = sp[q] - l[q - 1]  # 7 - 1 = 6
#             # .     21         6     =   15
#             #      35         15.    =.  20
#             l.append(zas)  # dobav6 : 1,6
#             # dobav 15: 1,6,15, 20
#             if zas == 1:
#                 break
#         spec.append(l)
#         return fun(l)
#
#     return [1]
#
#
# spis = [1, 7, 21, 35, 35, 21, 7, 1]
# spec = [spis]
# m = int(input("what line? "))
# fun(spis)
# spec.append([1])
# print(*spec[-m])