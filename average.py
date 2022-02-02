from tkinter import*

window = Tk()
window.title("Calculator")
window.geometry("500x250")

result = StringVar()

def Calculate():
    try:
        Eqation = entry_eqation.get()
        total = str(eval(Eqation))
        print (total)
        result.set(total)
    except ZeroDivisionError:
        result.set('Error')
    except SyntaxError:
        result.set('Error')
    except NameError:
        result.set('Error')
        
        
    

label = Label(window,text="Eqation",font=('Consolas',25))
label.pack()
entry_eqation = Entry(window,font=('Consolas',25))
entry_eqation.pack()
label = Label(window,textvariable=result,font=('Consolas',25),bg="white")
label.pack()
Calculate = Button(window,text="Calculate the equation",font=('Consolas',25),command=Calculate)
Calculate.pack()
window.mainloop()
