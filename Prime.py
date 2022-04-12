num = int(input("Enter a Number:"))
if num > 1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is not a Prime Number")
            break
    else:
            print(num, "is a Prime Number")
else:
    print(num,"is not a Prime Number")