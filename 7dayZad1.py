# Задание 1
# for x in '0123456789abcde':
#     x1 = '123' + str(x) + '5'
#     x2 = '1' + str(x) + '233'
#     res = int(x1, 15) + int(x2, 15)
#     if res % 14 == 0:
#         res = res // 14
#         print(res)
#         break

# Задание 2
# num1_digits = [10, 11, 2, 6, 7, 13, 1]
# num2_digits = [15, 0, 2, 4, 10, 8, 9]
#
# total_sum = sum(num1_digits) + sum(num2_digits)
#
# for p in range(16, total_sum + 2):
#     if total_sum % (p - 1) == 0:
#         print(p)

# Задание 3
# for x in range(10):
#     x1 = str(x) + 'b' + '0' + '9'
#     x2 = str(x) + '8' + 'e' + '8'
#     res = int(x1,17) + int(x2, 15)
#     if res % 155 == 0:
#         res = res // 155
#         print(res)
#         break


# Задание 4
# nones = False
# for y1 in range(11):
#     for x1 in range(11):
#         for x2 in range(8):
#             for y2 in range(8):
#                 a = str(y1) + '04' + str(x1) + '5'
#                 b = '253' + str(x2) + str(y2)
#                 res = int(a, 11) + int(b, 8)
#                 if res % 117 == 0:
#                     res = res // 117
#                     print(res)
#                     nones = True
#                     break
#             if nones:
#                 break
#         if nones:
#             break
#     if nones:
#         break


# Задание 5
# a = 7*(512**1912) + 6*(64**1954) - 5*(8**1991) - 4 * (8**1980) - 2022
# s = ""
# while a != 0:
#     s += str(a % 8)
#     a //= 8
# s = s[0:]
# print(s.count("7"))

