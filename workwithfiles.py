f=open("OpenData_Slovakia_Covid_PositiveTests_AgeGroup_District_mini.csv",encoding="UTF-8")

lines=f.readlines()
m = 0
z = 0
mesta=[]
pocet=[]
mesto ={}
max = 0
loc = "a"
vek={}
for a in lines:
    a = a.rstrip() #  rozdeli na riatky stringov
    data = a.split(";") #  rozdeli na pole delen ;
    if data[3] in mesto:
        mesto[data[3]]+=1
    else:
        mesto[data[3]]=1 
print (mesto)
for k , v in mesto.items():
    print (k,v)
    if v > max:
        max = v
        loc = k
    else :
        continue
print ("najviac nakazenich mesto ",max,loc)

for z in lines:
    z = z.rstrip() #  rozdeli na riatky stringov
    data = z.split(";") #  rozdeli na pole delen ;
    if data[4] in vek:
        vek[data[4]]+=1
    else:
        vek[data[4]]=1
print (vek)


# for a in lines:
#     a = a.rstrip() #  rozdeli na riatky stringov
#     data = a.split(";") #  rozdeli na pole delen ;


# for l , k in mesta:
#     print(mesta[k])
#     print(pocet[k])       
      
# for a in lines:
#     a = a.rstrip() #  rozdeli na riatky stringov
#     print(a)
#     data = a.split(";") #  rozdeli na pole delen ;
#     if data[2] == "Muž":
#         m=m+1
#     if data[2] == "Žena":
#         z=z+1


# for x,y in enumerate(lines):
#     if x < 100:
#         print(y)
#         print(x)
#         continue
#     if x == 100:
#         break
    

# for i in lines:
#     i = i.rstrip()
#     print (i)
