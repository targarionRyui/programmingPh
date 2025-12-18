
# Задание 1
# n = int(input())
# l = [0,1]
#
# for i in range(n-2):
#     new = l[0] + l[1]
#     l[0] = l[1]
#     l[1] = new
#
# print(l[1])
#
#
#
# Задание 2
# n = int(input())
#
# l = [0,1,1]
#
# for i in range(n-3):
#     new = l[0] + l[1] + l[2]
#     l[0] = l[1]
#     l[1] = l[2]
#     l[2] = new
#
# print(l[2])



# Задание 3

c = [
    [0,1,1,1,1,1],
    [0,0,0,0,0,1],
    [0,40,70,0,0,1],
    [100,0,0,0,0,1]
]

for i in range(len(c)):
    for j in range(len(c[0])):
        c[i][j] = [c[i][j]]

for i in range(len(c)):
    for j in range(len(c[0])):
        if i == 0 and j == 0:
            continue
        elif i == 0 and j != 0:
            c[i][j][0] = c[i][j][0] + c[i][j - 1][0]
            c[i][j][1::] = c[i][j - 1][1::] + [" Right "]

        elif i != 0 and j == 0:
            c[i][j][0] = c[i][j][0] + c[i - 1][j][0]
            c[i][j][1::] = c[i - 1][j][1::] + [" Down "]

        else:
            if c[i - 1][j][0] > c[i][j - 1][0]:
                c[i][j][0] = c[i][j][0] + c[i - 1][j][0]
                c[i][j][1::] = c[i - 1][j][1::] + [" Down "]
            elif c[i - 1][j][0] < c[i][j - 1][0]:
                c[i][j][0] = c[i][j][0] + c[i][j - 1][0]
                c[i][j][1::] = c[i][j - 1][1::] + [" Right "]

print(c[len(c) - 1][len(c[0]) - 1])
            
            
            
            