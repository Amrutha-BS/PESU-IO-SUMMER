'''5)To find whether string is numeric'''
print("//program to find whether a string is numeric//")
a=input("enter a string:")
n=len(a)
count=0
for i in a:
    if i.isdigit():
        count=count+1
if count==n:
    print("the string is numeric")
else:
    print("the string is not numeric")
input("press enter to exit:")
