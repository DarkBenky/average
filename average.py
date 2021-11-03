from typing import List

str='''gfhfjh ghfjhfj
hmjgjg gfhfjh ghfjhfj
hmjgjg gfhfjh ghfjhfj
hmjgjg'''


d={}
for i in str:
    if i in d:
        d[i]=d[i]+1
    else :
        d[i]=1 
print (d)        
a = 1

for i in str: 
    if i == ' ':
        a = a + 1
print ('\n')

boha = 1
for i in str: 
    if i == '\n':
        boha = boha + 1
        a = a + 1
print ('\n')
print ('riadkov :' ,boha)
print ('\n')
print ('slov :' , a)
