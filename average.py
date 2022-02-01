car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
def set(key, value):
    global car
    car[key] = value
    print(car)

def check():
    global car
    _MAX_LENGTH = 4
    length = len(car)
    if length == _MAX_LENGTH:
        for key in car:
            car.pop(key)
            break
        print(car)

set("logo","BMW")
check()
set("logo1","BMW1")


uloha5(x,z)
