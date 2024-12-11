#  A program that converts a unit (e.g kilometers to miles, celsius to fahrenheit)

# Algorithm
# Display section for conversion (vol, mass, temp)
# Get the option picked by the user
# display the avaliable conversion for each section
# get the value to be converted
# carry out the conversion
# display the image 

print("Welcome to Zen unit conversion program")
print()
print("***********************")
print("Choose a conversion type:")
print("1. Length")
print("2. Mass")
print("3. Temperature")
print("***********************")
print()
option = int(input("choose an option: "))

if option == 1:
    print("Below is the available conversion")
    print()
    print("***********************")
    print("1. Inches to Millimeters")
    print("2. Millimeters to Inches")
    print("***********************")
    print()
    length_option = int(input("choose an option: ")) 

elif option == 2 :
    print("Below is the available conversion")
    print()
    print("***********************")
    print("1. Kilograms to Pounds")
    print("2. Grams to Ounces")
    print("***********************")
    print()
    mass_option = int(input("choose an option: "))

elif option == 3 :
    print("Below is the available conversion")
    print()
    print("***********************")
    print("1. Celsuis to Farenheight")
    print("2. Farenheight to Celsuis")
    print("***********************")
    print()
    temp_option = int(input("choose an option: "))

else: 
    print("Invalid option, please choose again")