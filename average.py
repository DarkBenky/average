def rozbit():

    x = '10*5+8+20'
    
    nums = []
    znaminka=[]
    last_index=-1

    for i , c in enumerate(x):
        if c =='+' or c =='-':
            nums.append(x[1+last_index:i])
            znaminka.append(c)
            last_index = i

    nums.append(x[1+last_index:])
    return nums,znaminka
      
print(rozbit())


