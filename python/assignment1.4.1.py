################################################################################################
#Write a program that prints Even numbers from 1 to a number given by the user 
#then print the Sum (total) of them in the end.

#Example:
#Enter the last number of the range: 20
#The even numbers are 2, 4, 6, 8, 10,
###############################################################################################

try:

    #Taking user input
    last = input("Enter the last number of  the range: ")
    last = int(last)

    #Initialising the variables
    start = 1
    total = 0

    # iterating each number in list
    for num in range(start, last + 1):

        # checking condition
        if num % 2 == 0:
            print(num, end=" ")

            #new sum = previous sum + number of even
            total = total + num

    #printing the sum of the even numbers
    print("\nThe sum of these numbers is:",total)

except:
    print("Please enter numeric number only.")
