# 1 Задание

# count = 0
# maxS = 0
# with open("39762.txt", "r") as f:
#     n = f.read().split()
#     n = [int(i) for i in n]
#
#     for i in range(len(n) - 1):
#         a = n[i]
#         b = n[i+1]
#         if (a * b) % 15 == 0 and (a + b) % 7 == 0:
#             count += 1
#             if a + b > maxS:
#                 maxS = a + b
#     print(count, maxS)



# 2 Задание

# with open("68279.txt", "r") as f:
#     n = [int(i) for i in f.readlines()]
#     countOR = 0
#     sumOR = 0
#     max_562 = max(num for num in n if num % 1000 == 562)
#
#     for i in range(len(n) - 3):
#         sumAL = 0
#         countVR = 0
#         a = n[i]
#         b = n[i + 1]
#         c = n[i + 2]
#         d = n[i + 3]
#         sp = [a, b, c, d]
#         for j in sp:
#             if (j < 100000) and (j > 9999):
#                 countVR += 1
#         if (countVR > 0) and (countVR < 3):
#             count3 = 0
#             count7 = 0
#             for j in sp:
#                 if j % 3 == 0:
#                     count3 += 1
#                 if j % 7 == 0:
#                     count7 += 1
#             if count3 < count7:
#                 sumAL = a + b + c + d
#                 if (sumAL > max_562) and (sumAL < (max_562 * 2)):
#                     countOR += 1
#                     if sumAL > sumOR:
#                         sumOR = sumAL
#     print(countOR, sumOR)



# 3 Задание

# with open("40992.txt", "r") as f:
#     n = [int(i) for i in f.readlines()]
#     countPara = 0
#     maxSum = 0
#     vr = [i for i in n if i % 2 != 0]
#     srAR = sum(vr) / len(vr)
#     for i in range(len(n) - 1):
#         sp1 = n[i:i+2]
#         count1 = 0
#         count2 = 0
#         for j in sp1:
#             if j % 5 == 0:
#                 count1 += 1
#             if j < srAR:
#                 count2 += 1
#             if count1 > 0 and count2 > 0:
#                 countPara += 1
#                 maxSum = max(maxSum, sum(sp1))
#                 break
#     print(countPara, maxSum)




