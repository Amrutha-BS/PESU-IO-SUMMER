'''4)SUM OF DIGITS'''
print("//program to find sum of digits of an integer//")
a=int(input("enter a number:"))
sum=0
while a!=0:
  n=a%10
  sum=sum+n
  a=a//10
print(sum)
input("press enter to exit:")
