#############################################################################################################################################
Write a program that accepts a Malaysian city from the user and displays a tourist attraction of that city as follows:
City             Monument
KL               Petronas Twin Towers
Selangor    Batu Caves
Penang      Penang Hill
Kedah         Langkawi SkyCab
############################################################################################################################################
#Taking user input
malaysian_city = input("Please enter a City from Malaysia (KL/Selangor/Penang/Kedah):")

city = malaysian_city.lower()

#printing the city and monument
print("City" +"\t\t" + "Monument")

if city =="kl" or city == "selangor" or city == "penang" or city == "kedah" :

    #if user input KL
    if city == "kl":
        print(city +"\t\t" + "Petronas Twin Towers")

    #if user input selangor
    elif city == "selangor":
        print(city +"\t" + "Batu Caves")

    #if user input penang
    elif city == "penang":
        print(city + "\t\t" +"Penang Hill")

    else :
        print(city+ "\t\t" +"Langkawi SkyCab")

else:
    print("The city is not in the list")