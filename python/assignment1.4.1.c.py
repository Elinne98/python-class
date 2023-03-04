################################################################################
#Write a Python program that KEEPS taking the input from the user and print it 
#until the user enters the word "stop", it stops and exits the program.
################################################################################

###looping
while True:

    #Taking user input
    word = input("Enter a word:")

    #if user enter stop
    if word == "stop":

        #breaking "while True" loop (exiting the program)
        break

    print(word)

    #continuing to ask input from user
    continue

##looping Ends#################

##outside the loop section#####
print("Thank you")