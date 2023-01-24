#Accept a sequence of five single digit numbers separated by commas as input. Print the product of all five numbers.
str=input()
pro=1
for i in range(0,9,2):
    y=int(str[i])
    pro*=y
print(pro)
