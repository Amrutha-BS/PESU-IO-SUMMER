'''3)program to find even numbers in a given list'''
print("//program to print even numbers in a given list and to stop printing when compiler meets 237//")
l=[386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,162,758,219,918,237,412,566,826,248,866,950,626,949,687,217,815,67,104,58,512,24,892,894,767,553,81,379,843,831,445,72,717,958,743,527]
for i in l:
    if i==237:
      input("press enter to exit:")
      exit()
    elif i%2==0:
         print(i)
input("press enter to exit:")
