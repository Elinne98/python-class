####################################################################################################################################################################################
#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade >= 0.9 A ,>= 0.8 B, >= 0.7 C, >= 0.6 D ,< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
#####################################################################################################################################################################################

#Taking user input score
user_score = input("Please enter Score: ")

try:
    score = float(user_score)

    # if the score above 1.0, then print out of range
    if score < 0 or score > 1.0 :
        print("Error:score out of range!")

    #if user enter score above or equal to 0.9, then print A
    elif score >= 0.9 :
        print("A")

    #if user enter score above or equal to 0.8, then print B
    elif score >= 0.8 :
        print("B")

    #if user enter score above or equal to 0.7, then print C
    elif score >= 0.7 :
        print("C")

    #if user enter score above or equal to 0.6, then print D
    elif score >= 0.6 :
        print("D")

    #if user enter score above or equal to 0.6, then print D
    else:
        print("F")

except:
    print("Error.Please enter a number from 0.0 to 1.0")


