######################################################################################################################################################
#Create a program that prompts the user for integer numbers till the user enters the word 'done.' 
#Once you've entered 'done,' print the biggest and lowest of the numbers. 
#If the user enters anything other than a valid number, use a try/except to catch it and display an appropriate message before ignoring the number.
#######################################################################################################################################################

biggest = None
smallest = None

####looping begins###############################
while True:

    #testing whether the input is number
    try:

        # Taking user input
        number = input("Please enter a number:")

        #if user enter done
        if number == "done":
            break

        # Converting to integer
        num = int(number)

        if biggest is None or num > biggest:
            biggest = num

        elif smallest is None or num < smallest:
            smallest = num

    except:
        #printing error message
        print("Sorry! You entered a text.Please enter a number again.")
        continue

###looping ends###############
#printing the biggest and smallest number
print("Thank you.The program finishes")
print("The biggest number is ", biggest)
print("The smallest number is ", smallest)