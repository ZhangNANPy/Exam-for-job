n = str(bin(int(input(), 10)))[2:]
flag = '1'
p = 0
tempList = [0]
for i in range(len(n)):
    if n[i] == flag:
            tempList[p] += 1
    else:
        if flag == '0':
            flag = '1'
            p += 1
        else:
            p += 1
            flag = '0'
        tempList.append(1)
if flag == '1':
    del tempList[len(tempList) - 1]
re = 1
for i in tempList:
    re *= i
print(re + int(len(tempList)/2))