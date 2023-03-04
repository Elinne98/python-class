#############################################################################################################
#Write a Python calculator that does the following with two numbers:
#1) addition (ex: a + b)
#2) subtraction (ex: a-b)
#3) Multiplication (ex: a*b)
#4) Division (ex: a/b)
#5) exit the calculator.
#- The program keeps providing the user with a menu with options from 1 to 5.
#- if the user chooses an option from 1 to 4,  the user enters the numbers a and b. then gets the result.
#- if the user chooses the number 5 option, then the calculator exits.
#############################################################################################################

# function addition of two numbers
def add(a, b):
    return a + b

# function subtraction of two numbers
def subtract(a, b):
    return a - b

# function multiplication of two numbers
def multiply(a, b):
    return a * b

# function division of two numbers
def divide(a, b):
    return a / b

#printing the options
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exit")

### looping begins ###################################################
while True:

   # take input from the user
    choice = input("Enter your choice(1/2/3/4/5): ")

    if choice == '5':
        break

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))

        except:
            print("You might have entered a non numeric value")

    else:
        print("Please choose an option from 1 to 5 only.")

##  looping ends  ######################################
print("Thank you. bye")