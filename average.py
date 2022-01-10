
import tkinter
import random

def uloha():
    x = ''
    x1 = '*'
    for i in range(0,10):
        x = x + x1
    print(x)
    print("SPSE")
    print("Zochova")
    print (x)


def uloha2():
    x3=tkinter.Canvas(bg='black',width = 400 , height = 400)
    x3.pack()

    x = random.randint(100,300)
    y = random.randint(100,300)

    x1 = random.randint(100,300)
    y1 = random.randint(100,300)


    x3.create_text(x,y,text='SPSE',fill='gold')
    x3.create_text(x1,y1,text='Zochova',fill='gold')
    x3.mainloop()



def uloha3(x):
    z =''
    for i in range(0,x):
        z = z + "@"
    print (z)


x = int(input('Enter'))
uloha3(x)


def uloha4(x):
    x1= "*"
    for i in range(0,x):
        print(x1)
        x1 = x1 + "*"

uloha4(x)

def uloha5(x,z):
    x3=tkinter.Canvas(bg='black',width = 400 , height = 400)
    x3.pack()

    
    

    
    for i in range(0,x+1):
        x1 = random.randint(20,380)
        y1 = random.randint(20,380)

        x = random.randint(20,380)
        y = random.randint(20,380)

        
        x3.create_rectangle(x1,y1,x,y,fill=z)

    x3.mainloop()    

z = input("color")

uloha5(x,z)
