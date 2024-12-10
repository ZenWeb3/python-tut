# user_Name =  input("What is your Name?" )
# user_Age = input("How old are you?" )

# print ("Welcome", user_Name, "You are " + user_Age + " Years old")

mood = input("How are you feeling? (Happy, Sad) ")
age = input("How old are you? ")
age = int(age)

if mood == "happy" and age >= 18:
    print("Its always good to be happy!")
elif mood == "Sad" and age >= 18:
     print("It's not good to be Sad! ")
elif age < 18 :
     print("You are too young to be on this program")
else: 
     print("Choose based of the options above ")