#################################################################################################################################################################################
#Write a program to prompt the user for hours and rate per hour to compute the gross pay.
#1)The Payment should be the normal rate for hours up to 40 and time-and-a-half of the hourly rate for hours above 40.
#2)Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value.
#3)Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
#4)You should use input to read a string and float() to convert the string to a number.
#Do not worry about error checking of the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.
##################################################################################################################################################################################

#########################
#Function Area
#########################

# computepay function
def computepay(work_hrs, rate):

    #if working hours is in range 0 to 40
    if work_hrs > 0 and work_hrs <=40:
        pay = float(work_hrs*rate)
        return pay

    #if the hourly rate for the hours below 40
    elif work_hrs > 40 :
        pay = 40 * rate + (work_hrs - 40) * 1.5 *rate
        return pay

    else:
        #if user enter any invalid number such as negative or string
        print("Please enter positif numbers only")
        return -1

#Taking user input
working_hours = input("Please Enput the working hours:")

#Taking user input
hourly_rate = input("Please Enput the hourly rate:")

try:

    #converting to float
    work_hrs = float(working_hours)
    rate = float(hourly_rate)


    pay = computepay(work_hrs,rate)
    if pay >= 0:
        print("Your gross salary is:RM",pay)

except :
    print("Please input a valid number")



