############################################################################################################
#Write a program that asks the user for  1) The current temperature in  °C  ,2) The time (day or night) 
#The program tells how is the weather like, as follows:
#Day time:30 to 33  °C  --> Normal, below 30  °C   --> Cold, higher than 33 °C  --> Hot
#Night time:26 to 28 °C  --> Normal, below 26 °C   --> Cold, higher than 28 °C  --> Hot
#############################################################################################################

#Taking user  input
time = input('Please enter "Day" or "Night":')

#Taking user input
temperature = input("Please enter the current temperature:")

if time == "Day" or time =="Night":
    try:
        temp = float(temperature)

        #If user enter "Day"
        if time == "Day":

            #if user enter below or equal to 33 and temperature above or equal to 30, then print the message
            if temp <=33 and temp>=30:
                print("It is a Normal Day!")

            #if user enter temperature below 30, then print the message
            elif temp < 30:
                print("It is a Cold Day!")

            else:
                print("It is a Hot Day!")

        else :

            #if user enter below or equal to 28 and temperature above or equal to 26, then print the message
            if temp<= 28 and temp>=26 :
                print("It is a Normal Night!")

            #if user enter temperature below 27, then print the message
            elif temp < 26:
                print("It is a Cold Night")

            else:
                print("It is a Hot Night!")

    except:
        print("Error:Please input the correct temperature")

else:
    print("please input the right time!")

print("Goodbye!")