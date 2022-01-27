arr = [32, 67, 88, 13, 50]
max = 0
min = 100

for i in arr:
    if i > max:
        max = i
    if i < min:
        min = i
print (min, max)
