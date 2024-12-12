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

    if length_option == 1:
        inches_value = int(input("Enter your inches value: "))
        # 1 inch = 2.540 centimeters
        mm_value = inches_value * 2.540
        print()
        print("Your inches value ", inches_value, "inches in centimeter is ", mm_value )
    
    elif length_option == 2:
        mm_value = int(input("Enter your millimeter value: "))
        # 1 millimeter =  0.03937 inches
        inches_value = mm_value * 0.03937
        print()
        print("Your millimeter value ", mm_value, "mm in inches is ", inches_value )

elif option == 2 :
    print("Below is the available conversion")
    print()
    print("***********************")
    print("1. Kilograms to Pounds")
    print("2. Grams to Ounces")
    print("***********************")
    print()
    mass_option = int(input("choose an option: "))

    if mass_option == 1:
        kilo_value = int(input("Enter your kilo value: "))
        # 1 kilogram = 2.20462 pounds
        pound_value = kilo_value * 2.20462
        print()
        print("Your kilogram value ", kilo_value, "kg in pounds is ", pound_value )

    elif mass_option == 2:
        gram_value = int(input("Enter your gram value: "))
        # 1 gram = 0.00220462 ounces
        ounce_value = gram_value * 0.00220462
        print()
        print("Your gram value ", gram_value, "g in ounces is ", ounce_value )

elif option == 3 :
    print("Below is the available conversion")
    print()
    print("***********************")
    print("1. Celsuis to Farenheight")
    print("2. Farenheight to Celsuis")
    print("***********************")
    print()
    temp_option = int(input("choose an option: "))

    if temp_option == 1:
        celsuis_value = int(input("Enter your celsuis value: "))
        # 1 celsius = 9/5 * fahrenheit + 32
        farenheit_value = (9/5) * celsuis_value + 32
        print()
        print("Your celsius value ", celsuis_value, "°C in fahrenheit is ", farenheit_value )

    elif temp_option == 2:
        farenheit_value = int(input("Enter your fahrenheit value: "))
        # 1 fahrenheit = 5/9 * (celsius - 32)
        celsuis_value = (5/9) * (farenheit_value - 32)
        print()
        print("Your fahrenheit value ", farenheit_value, "°F in celsius is ", celsuis_value )

else: 
    print("Invalid option, please choose again")