a = 1
x = 1
y = 1
w = int(input('width'))
h = int(input('lenght'))
r =[[0]*w for i in range(0,h)]
while a == 1:
    for riadok in r:
        print(riadok)
    print('hrac1') 
    x=int(input('x'))
    y=int(input('y'))
    if r[x][y]==0:
        r[x][y]=1
    for riadok in r:
        print(riadok)
    print('hrac2')   
    x=int(input('x'))
    y=int(input('y'))
    if r[x][y]==0:
        r[x][y]=2
    for riadok in r:
        cislo = 3
        pocet = 0
        
         
        
