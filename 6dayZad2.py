# Задание 1
# with open("27686.txt", "r") as f:
# 	symbols = f.read()
# 	countX = 0
# 	bestX = 0
# 	for i in range(len(symbols)):
# 		if symbols[i] != 'X':
# 			countX = 0
# 		else:
# 			countX += 1
# 		if countX > bestX:
# 			bestX = countX
# 	print(bestX)



# Задание 2
# with open("36037.txt", "r") as f:
# 	symbols = f.read()
# 	count = 0
# 	best = 0
# 	for i in range(len(symbols)-4):
# 		sp = [symbols[i],symbols[i+1],symbols[i+2],symbols[i+3]]
# 		if sp[0] == 'X' and sp[1] == 'Z' and sp[2] == 'Z' and sp[3] == "Y":
# 			count = 0
# 			i += 4
# 		else:
# 			count += 1
# 		if count > best:
# 			best = count
# 	print(best)


# Задание 3
# with open("46982.txt", "r") as f:
#     s = f.read()
#     s = s.split('E')
#
#     print(len([x for x in s[0:] if len(x) >=12 and not 'F' in x]))
