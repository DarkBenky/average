def write():
    f = open("data.txt","a")
    
    date = input("date :")
    todo = input("to do :")
    
    todo = todo.replace(" " , "_")
    f.write(date+"|")
    f.write(todo)
    f.write("\n")
    


def read():
    
    f = open("data.txt","r")
    
    for line in f:
        data = line.split("|")



def search():
     
    search = input("input searched date :")
    
    f = open("data.txt","r")
    
    for line in f:
        data = line.split("|")
        if data[0] == search:
            print ("V tento den ste chceli urobi" , data[1])


while True:
    x = input("input if you want write (write) or search (search) or read (read) all thinks :")
    
    if x == "write":
        write()
    elif x == "search":
        search()
    elif x == "read":
        read()    
            
