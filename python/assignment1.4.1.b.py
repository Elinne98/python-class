#########################################################################################################################
#Write a Python program which iterates from 1 to a number entered by a user (using input). 
#The program will print "Multi Three!" instead of the number,  for numbers that are multiples of three.
#The program will print "Multi Five!" instead of the number,  for numbers that are multiples of five.
#########################################################################################################################

#testing whether the input is integer
try:

    #Taking user input
    last = input("Enter the last number of  the range: ")
    last = int(last)

    #initialising
    start = 1

    # iterating each number in list
    for num in range(start, last + 1):

        #Checking the condition
        if num % 3 == 0:
            print(num, end =" ")
            print("multi three")

        if num % 5 == 0:
            print(num, end =" ")
            print("multi five")

        else:
            print(num)

except:
    #printing the error message
    print("Please enter numeric number only.")