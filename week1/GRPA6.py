'''
Accept two positive integers M and N as input. There are two cases to consider:

(1) If M < N, then print M as output.

(2) If M >= N, subtract N from M. Call the difference M1. If M1 >= N, then subtract N from M1 and call the difference M2. Keep doing this operation until you reach a value k, such that, Mk < N. You have to print the value of Mk as output.
'''

m=int(input())
n=int(input())
if n>m:
    print(m)
elif m>=n:
    m1=m-n
    if(m1>=n):
        m1=(m1-n)
        while m1>0:
            if m1>=n:
                m1=(m1-n)
                continue
            elif m1<n:
                break
print(m1)
