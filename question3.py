'''3)BINARY SEARCH'''
print("program to search a number in a list using binary search")
a=input("enter the numbers of the list separated by commas:")
n=int(input("enter the number to be searched"))
l=a.split(',')
count=0
for i in l:
        if int(i)==n:
          print("number found")
          print("the position of the number is:",l.index(i))
          count=1
if count==0:
   print("the number is not found") 
input("press enter to exit:")
