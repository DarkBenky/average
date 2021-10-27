def rozbit():

    x = '10*5/4+8+20*4'
    
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

def roz(x):

    nums = []
    znaminka=[]
    last_index=-1

    for i , c in enumerate(x):
        if c =='*' or c =='/':
            nums.append(x[1+last_index:i])
            znaminka.append(c)
            last_index = i

    nums.append(x[1+last_index:])
    return nums,znaminka

def zrataj(cisla,znaminka):
    print (cisla , znaminka)
    for i in znaminka:
        x = 0
        
        z=int(cisla[x])
        z1=int(cisla[x+1])
        q=znaminka[x]
        if q == '*':
            z2 = z  * z1
        if q == '/':
            z2 = z  / z1
        print (z2)    
        

x , y = rozbit()
print (x , y)
for i in x:
    x1 , y1 = roz (i)
    zrataj (x1 , y1)




