#You are given the dates of birth of two persons, not necessarily from the same family. Your task is to find the younger of the two. If both of them share the same date of birth, then the younger of the two is assumed to be that person whose name comes first in alphabetical order (names will follow Python's capitalize case format).
#The input will have four lines. The first two lines correspond to the first person, while the last two lines correspond to the second person. For each person, the first line corresponds to the name and the second line corresponds to the date of birth in DD-MM-YYYY format. Your output should be the name of the younger of the two.
n1=input()
a1=input()
n2=input()
a2=input()
d1=int(a1[:2])
m1=int(a1[3:5])
y1=int(a1[6:10])
s1=d1+(m1*10)+(y1*1000)
d2=int(a2[:2])
m2=int(a2[3:5])
y2=int(a2[6:10])
s2=d2+(m2*10)+(y2*1000)
n1=n1.lower()
n2=n2.lower()
if(s1>s2):
    print(n1.title())
elif(s1==s2):
    if(n1>n2):
        print(n2.title())
    else:
        print(n1.title())
else:
    print(n2.title())
