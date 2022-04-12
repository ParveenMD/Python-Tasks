year = int(input("Enter a year:"))
if(year %400==0) and (year % 100 == 0):
    print("{0} is Leap Year".format(year))
elif(year %4 ==0) and (year % 100!=0):
    print("{0} is Leap Year".format(year))
else:
    print("{0} is Not a Leap Year".format(year))