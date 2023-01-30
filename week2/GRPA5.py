#Accept a string as input. Your task is to determine if the input string is a valid password or not. For a string to be a valid password, it must satisfy all the conditions given below:

#(1) It should have at least 8 and at most 32 characters

#(2) It should start with an uppercase or lowercase letter

#(3) It should not have any of these characters: / \ = ' "

#(4) It should not have spaces

#It could have any character that is not mentioned in the list of characters to be avoided (points 3 and 4). Output True if the string forms a valid password and False otherwise.

str=input()
flag=0
if(len(str)>=8 and len(str)<=32):
    flag=1
elif(str[0].isdigit):
    flag=0
l=["/","\\","=","\'","\""]
for x in str:
    if x in l:
        flag=0
    elif x==" ":
        flag=0
if flag==1:
    print("True")
elif flag==0:
    print("False")
