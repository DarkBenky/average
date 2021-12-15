f=open("susr-dataset-objednavky-pipes.csv",encoding="UTF-8")

lines=f.readlines()
price = 0
num = 0
firmy = {}
for z in lines:
    z = z.rstrip() #  rozdeli na riatky stringov
    data = z.split("|") #  rozdeli na pole delen ;
    price = price + float(data[9])
    num = num +1
price = price / num
print ("primerne cena je",price)
max = 0
firma =""
for z in lines:
    z = z.rstrip() #  rozdeli na riatky stringov
    data = z.split("|") #  rozdeli na pole delen ;
    if float(data[9]) > max:
        max = float(data[9])
        firma =data[4]
print ("maximalna cena za objednavku je",max ,"od firmy",firma)

for a in lines:
    a = a.rstrip() #  rozdeli na riatky stringov
    data = a.split("|") #  rozdeli na pole delen ;
    if data[4] in firmy:
        firmy[data[4]] +=1
    else:
        firmy[data[4]]=1 
      
m = 0
f = ""
for k , v in firmy.items():
    
    if v > m:
        m = v
        f = k
    else:
        continue    
print ("najviac objednavok ma",f,"a to",m)

cena = 0

m1 = 0
f1 = 0

for a in lines:
    a = a.rstrip() #  rozdeli na riatky stringov
    data = a.split("|") #  rozdeli na pole delen ;
    if data[4] in firmy:
        cena = float(data[9])
        firmy[data[4]] +=cena
    else:
        firmy[data[4]] =cena        
           
for k , v in firmy.items():
    
        if v > m1:
            m1 = v
            f1 = k
        else:
            continue
print ("najvecie cenu objedanavok ma firma", f1 , "a to" , m1)        
            
