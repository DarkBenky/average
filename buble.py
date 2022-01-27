
arr = [0,564,56,78,5,69,56]

for i in range(len(arr)):
    for j in range(i):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print (arr)
