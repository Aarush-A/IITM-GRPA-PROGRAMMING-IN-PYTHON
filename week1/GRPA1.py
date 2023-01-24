#Accept five words as input and print the sentence formed by these words after adding a space between consecutive words and a full stop at the end.
str1=""
space=" "
end="."
for i in range(4):
    str2=input()
    str1+=str2
    str1+=space
str2=input()
str1+=str2
str1+=end
print(str1)
