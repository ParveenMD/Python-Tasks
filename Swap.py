var1= int(input("Enter value of var1:"))
var2= int(input("Enter value of var2:"))
print("\nBEFORE SWAPPING(Actual Value of var):Value of var1:{}".format(var1))
print("BEFORE SWAPPING(Actual value of var):Value of var2:{}".format(var2))
temp_var=var1
var1=var2
var2=temp_var
print("\nAFTER SWAPPING:Value of var1:{}".format(var1))
print("AFTER SWAPPING:Value of var2:{}".format(var2))