##############################################################################################################################################################################
#Write a simple calculator ((((using functions))))) that takes 4 numbers (num1,num2,num3,num4) from the user and does the following for (num1 & num2) and then (num3 & num4):
#1) Adding 2 numbers
#2) Substracting for 2 numbers
#3) Multiplication for 2 numbers
#4) Division for 2 numbers
#5) Average of 2 numbers
#6) The sum of the results of the operations + , - , *, and / of the 2 numbers
#Note:
#1) You should handle the exception thrown in converting & division by zero.
#2) Negative values are ACCEPTED.
#3) Any extra processing is counted as a bonus for you.
##############################################################################################################################################################################

#Function of adding of the two numbers
def add(x, y):
    return x + y

#Function of subtraction of the two numbers
def subtract(x, y):
    return x - y

#Function of multiplies of the two numbers
def multiply(x, y):
    return x * y

#Function of division of the two numbers
def divide(x, y):
    a = x / y
    return a
#Function of average of the two numbers
def average(x, y):
    return (x + y) / 2

#Function of the sum of the results of the operations + , - , *, and / of the 2 numbers
def sums(x, y):
    return add(x, y) + subtract(x, y) + multiply(x, y) + divide(x, y)

######################################################
#Main Program
#######################################################
try:
    #Taking user input
    num1 = input("Please enter the first number:")
    num1 = float(num1)

    num2 = input("Please enter the second number:")
    num2 = float(num2)

    num3 = input("Please enter the third number:")
    num3 = float(num3)

    num4 = input("Please enter the fourth number:")
    num4 = float(num4)

except:
    print("please input valid numbers")

#printing the addition of num1 & num2, then num3 & num4
result1 = add(num1,num2)
print("The addition of num1 and num2 is:", result1)
result2 = add(num2,num3)
print("The addition of num3 and num4 is:",result2)

#printing the subtraction of num1 & num2, then num3 & num4
result3 = subtract(num1,num2)
print("\nThe subtraction of num1 and num2 is:",result3)
result4 = subtract(num3,num4)
print("The subtraction of num3 and num4 is:",result4)

#printing the multiplication of num1 & num2, then num3 & num4
result5 = multiply(num1,num2)
print("\nThe multiplication of num1 and num2 is:",result5)
result6 = multiply(num3,num4)
print("The multiplication of num3 and num4 is:",result6)
try:
    #printing the division of num1 & num2, then num3 & num4
    result7 = divide(num1,num2)
    print("\nThe division of num1 and num2 is:",result7)
    result8 = divide(num3,num4)
    print("The division of num3 and num4 is:",result8)

    #printing the sum of the results of the operations + , - , *, and / of the 2 numbers
    sum_numbers1 = sum(num1,num2)
    print("\nThe sum of the results:", sum_numbers1)
    sum_numbers2 = sum(num3,num4)
    print("The sum of the results:", sum_numbers2)
except:
    print("Division by zero. You might have entered a zero value.")

#printing the average of num1 & num2, then num3 & num4
result9 = average(num1,num2)
print("\nThe average of num1 and num2 is:",result9)
result10 = average(num3,num4)
print("The average of num3 and num4 is:",result10)



