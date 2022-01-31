
         
        
from tkinter import *


def button_pressed(number):
    global eqation_text 
    eqation_text = eqation_text + str(number)
    eqation_label.set(eqation_text)

def equals():
    global eqation_text
    
    try:
        
        total = str(eval(eqation_text))
    
        eqation_label.set(total)
    
        eqation_text = total
    except ZeroDivisionError:
        
        eqation_label.set('error')
        eqation_text = '' 
    
    except SyntaxError:
        
        eqation_label.set('error')
        eqation_text = '' 
          
    
def clear():
    
    global eqation_text
    eqation_text = ''
    eqation_label.set(eqation_text)
        
    

window = Tk()
window.title("Calculator")
window.geometry("700x600")

eqation_text = ''

eqation_label = StringVar()

label = Label(window, textvariable = eqation_label ,font = ("consolas",20), bg = 'white', width = 24 , height =2)
label.grid(row = 0, column = 4)


button1 = Button(window, text = 1 , height = 4 , width = 9 , font = 35 , command = lambda:button_pressed(1))
button1.grid(row= 1 , column = 1)
button2 = Button(window, text = 2 , height = 4 , width = 9 , font = 35 , command = lambda:button_pressed(2))
button2.grid(row= 1 , column = 2)
button3 = Button(window, text = 3 , height = 4 , width = 9 , font = 35 , command = lambda:button_pressed(3))
button3.grid(row= 1 , column = 3)
button4 = Button(window, text = 4 , height = 4 , width = 9 , font = 35 , command = lambda:button_pressed(4))
button4.grid(row= 2 , column = 1)
button5 = Button(window, text = 5 , height = 4 , width = 9 , font = 35 , command = lambda:button_pressed(5))
button5.grid(row= 2 , column = 2)
button6 = Button(window, text = 6 , height = 4 , width = 9 , font = 35 , command = lambda:button_pressed(6))
button6.grid(row= 2 , column = 3)
button7 = Button(window, text = 7 , height = 4 , width = 9 , font = 35 , command = lambda:button_pressed(7))
button7.grid(row= 3 , column = 1)
button8 = Button(window, text = 8 , height = 4 , width = 9 , font = 35 , command = lambda:button_pressed(8))
button8.grid(row= 3 , column = 2)
button9 = Button(window, text = 9 , height = 4 , width = 9 , font = 35 , command = lambda:button_pressed(9))
button9.grid(row= 3 , column = 3)
button0 = Button(window, text = 0 , height = 4 , width = 9 , font = 35 , command = lambda:button_pressed(0))
button0.grid(row= 4 , column = 1)
plus = Button(window, text = "+" , height = 4 , width = 9 , font = 35 , command = lambda:button_pressed("+"))
plus.grid(row= 4 , column = 2)
minus = Button(window, text = "-" , height = 4 , width = 9 , font = 35 , command = lambda:button_pressed("-"))
minus.grid(row= 4 , column = 3)
krat = Button(window, text = "*" , height = 4 , width = 9 , font = 35 , command = lambda:button_pressed("*"))
krat.grid(row= 5 , column = 1)
delene =Button(window, text = "/" , height = 4 , width = 9 , font = 35 , command = lambda:button_pressed("/"))
delene.grid(row= 5 , column = 2)
clear = Button(window, text = "clear" , height = 4 , width = 9 , font = 35 , command =clear )
clear.grid(row=5 , column = 3)
equal = Button(window, text ='=',height = 4 , width = 9 , font = 35 , command =equals)
equal.grid(row=6 , column = 1)
decimal = Button(window, text =".", height = 4 , width = 9 , font = 35 , command = lambda:button_pressed("."))
decimal.grid(row=6 , column =2)
window.mainloop()
