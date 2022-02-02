import random

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
def check():
    global car
    _MAX_LENGTH = 2
    length = len(car)
    if length >= _MAX_LENGTH:
        for key in car:
            car.pop(key)
            break
        print(car)
        
        
def check_all ():
    global car 
    MAX_LENGTH = 2
    length = len(car)
    MAX_LENGTH = length - MAX_LENGTH
    for i in range(MAX_LENGTH):
        check()
        
def set(key, value):
    global car
    car[key] = value
    print(car)


set("logo1","BMW1")
set("logo2","BMW2")
set("logo3","BMW3")
set("logo4","BMW4") 
check_all()




