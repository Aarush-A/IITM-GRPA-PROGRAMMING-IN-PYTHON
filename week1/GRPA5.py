#Accept two positive integers x and y as input. Print the number of digits in xy.
x=int(input())
y=int(input())
a=x**y
sum=0
while(a>0):
    c=a%10
    a-=c
    a/=10
    sum+=1
print(sum)
