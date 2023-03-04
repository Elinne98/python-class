###############################################################################################################################################################
#Write a Python program that asks the user for a number between 1 and 50 and it tells if it is Even or Odd.
#if the user enters a number that is outside the range 1-50, an alerting message will be displayed for them and the program will continue asking about numbers.
#If the user enters "finish", the program will stop.
###############################################################################################################################################################

#looping
while True:
    #Taking user input
    num= input("Please enter an integer between 1 and 50:")

    #if user input finish
    if num =="finish":
        break
    try:
        #converting to integer
        num = int(num)

        #checking the condition
        if num >= 1 and num <= 50 :
            #if the number is even
            if (num % 2 == 0):
                print("Your number is even.")

            #if the number is odd
            else:
                print("Your number is odd.")

        else:
            print("Please input number between 1 and 50.")

    except:
        print("\nPlease enter valid input")

        #keep taking the input from user
        continue

print("Thank you bye bye")
