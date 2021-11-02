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
    x = 0
    lol = 0
    for i in znaminka:
        z=int(cisla[x])
        z1=int(cisla[x+1])
        q=znaminka[x]
        if q == '*':
            z2 = z  * z1
            del cisla[x]
            x = x+1;
            cisla.insert(x,z2)
        if q == '/':
            z2 = z  / z1
            del cisla[x]
            x = x+1;
            cisla.insert(x,z2)
        res = []
        # vysledky si insertujem do pola
        res.insert(lol,z2)
        lol = lol + 1
        print (z2) 





x , y = rozbit()
print (x , y)
for i in x:
    x1 , y1 = roz (i)
    zrataj (x1 , y1)
