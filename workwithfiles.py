f=open("OpenData_Slovakia_Covid_PositiveTests_AgeGroup_District_mini.csv",encoding="UTF-8")

lines=f.readlines()
m = 0
z = 0
pohlavie = {}

mesto ={}
max = 0
loc = "a"
vek={}
vekkat =''
pocet = 0
for a in lines:
    a = a.rstrip() #  rozdeli na riatky stringov
    data = a.split(";") #  rozdeli na pole delen ;
    if data[3] in mesto:
        mesto[data[3]]+=1
    else:
        mesto[data[3]]=1 
print (mesto)
for k , v in mesto.items():

    if v > max:
        max = v
        loc = k
    else :
        continue
print ("najviac nakazenich mesto ",max,loc)

for z in lines:
    z = z.rstrip() #  rozdeli na riatky stringov
    data = z.split(";") #  rozdeli na pole delen ;
    if data[2] in pohlavie:
        pohlavie[data[2]]+=1
    else:
        pohlavie[data[2]]=1
print (pohlavie)

for z in lines:
    z = z.rstrip() #  rozdeli na riatky stringov
    data = z.split(";") #  rozdeli na pole delen ;
    if data[4] in vek:
        vek[data[4]]+=1
    else:
        vek[data[4]]=1
print (vek)

for x , y in vek.items():
    if y > pocet:
        pocet = y
        vekkat = x
    else :
        continue
print ("najviacia vekova kategoria je ",vekkat,pocet)

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