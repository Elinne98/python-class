###############################################################################################################################################################################
#Write a program into a file that has ".py" postfix to:
#Prompt/Ask the user for hours and rate per hour using input to compute gross pay.
#- Pay the hourly rate for the hours up to 40 and 50% more for all hours worked above 40 hours.
#- You should use input to read a string and float() to convert the string to a number.
#- You MUST process the error by printing a message and exiting the program if a user doesn't enter a numeric number like ("nine" instead of 9) by using Try - Except expression.
################################################################################################################################################################################

#Taking user input
working_hours = input("Please Enput the working hours:")

#Taking user input
hourly_rate = input("Please Enput the hourly rate:")

try:
    work_hrs = float(working_hours)
    rate = float(hourly_rate)

    #if working hours is in range 0 to 40
    if work_hrs > 0 and work_hrs <=40:
        pay = float(work_hrs*rate)
        print("Your Gross Pay Salary is :RM ",pay)

    #if the hourly rate for the hours below 40
    elif work_hrs > 40 :
        pay = 40 * rate + (work_hrs - 40) * 1.5 *rate
        print("Your gross salary is:RM", pay)

    #if user enter any invalid number such as negtive or string
    else:
        print("Please enter valid numbers only")

except :
    print("Please input a valid number")