def sortingLOL(num):
    for i in range(len(num)-1,0,-1):
        for lol in range(i):
            if num[lol]>num[lol+1]:
                temp = num[lol]
                num[lol]=num[lol+1]
                num[lol+1]=temp
num = [10,1,5,6,7,9]
sortingLOL(num)

print(num)
