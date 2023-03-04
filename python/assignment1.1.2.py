############################################################################################################
#Write a program that prints the largest number & smallest number out of 3 numbers entered by the user.
############################################################################################################
try:
    #Prompting the user for input
    number1 = input("please enter the first number:")
    number1 = float(number1)

    number2 = input("please enter the second number:")
    number2 = float(number2)

    number3 = input("please enter the third number:")
    number3 = float(number3)

    #supposing that number1 is biggest
    biggest_num = number1

    #find the biggest number of num1 and num2
    if number2 > number1:
        biggest_num = number2

    #find the biggest number of num3 and biggest num
    if number3 > biggest_num:
        biggest_num = number3

    #printing the largest number
    print("The largest number is : ", biggest_num)

    #supposing that number1 is smallest
    smallest_num = number1
    #find smallest number of num1 and num2
    if number2 < number1:
        smallest_num = number2

    #find the biggest number of num3 and smallest num
    if number3 < smallest_num:
        smallest_num = number3

    #printing the smallest number
    print("The smallest number is : ", smallest_num)

except:
    print("please enter a valid number only!")
