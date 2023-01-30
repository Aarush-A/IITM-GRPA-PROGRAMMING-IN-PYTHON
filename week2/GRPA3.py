#Accept a string as input and print the vowels present in the string in alphabetical order. If the string doesn't contain any vowels, then print the string none as output. Each vowel that appears in the input string — irrespective of its case — should appear just once in lower case in the output.
str=input()
str=str.lower()
l=["a","e","i","o","u"]
l2=[]
for i in range(len(str)):
    if str[i] in l:
        l2.append(str[i])
l2.sort()
l3=[]
for i in range(len(l2)):
    if l2[i] in l3:
        continue
    else:
        l3.append(l2[i])
for i in range(len(l3)):
    print(l3[i],end="")
if(len(l3)==0):
    print("none")
