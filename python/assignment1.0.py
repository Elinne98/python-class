##############################################################################################################################################
Please write a program that takes 2 numbers (number1 & number2) from the user (on the black screen) and prints 
1) The addition of number1 & number2
2) The substraction of number1 & number2
3) The multiplication of number1 & number2
4) The division of number1 by number2
5) The average of number1 & number2
6) The power of 2 of number1 and then number2
7) The sum of all the results from item 1) to item 6).

Important Note: after each printing of the items above, print a line of stars "*" to separate the printing and organize the output
##########################################################################################################################################
#Taking user input number
num1 = input("Enter first number:")

#Taking user input number
num2 = input("Enter second number:")

#Adding num1 and num2
sum_numbers = float(num1) + float(num2)

#substraction of num1 and num2
substr_numbers = float(num1) - float(num2)

#multiplication of num1 and num2
multi = float(num1)* float(num2)

#division of num1 and num2
div = float(num1) / float(num2)

#calculate average of num1 and num2
average_numbers = sum_numbers / 2

#calculate the power of 2 of number1 & number2
p1 = float(num1) ** 2
p2 = float(num2) ** 2

#calculate the sum of all the results
sum_results = sum_numbers + substr_numbers + multi + div + average_numbers + p1 + p2

#printing the addition of num1 and num2
print("The addition of number1 and number2 is:", sum_numbers)
print("*")

#printing the substraction of num1 and num2
print("The subtraction of number1 and number2 is:", substr_numbers)
print("*")

#printing num1 multiply by num2
print("The multiplication of number1 and number2 is:", multi)
print("*")

#printing the num1 divided by num2
print("The division of number1 and number2 is:", div)
print("*")

#printing the average of num1 and num2
print("The average number of number1 and number2 is :", average_numbers)
print("*")

#printing the power of 2 of number1
print("The power of 2 of number1 is:", p1)
print("*")

#printing the power of 2 of number2
print("The power of 2 of number2 is:", p2)
print("*")

#printing the sum of the results
print("The sum of all the results is:", sum_results)