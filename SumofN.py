def recursion_sum(num):
    if num<=1:
        return num
    else:
        return num+recursion_sum(num-1)
num =int(input("\nEnter a number to find the sum value:"))
sum_val =recursion_sum(num)
print("Sum of given number is:",sum_val)