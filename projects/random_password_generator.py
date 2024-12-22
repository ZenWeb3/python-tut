# A program that generates random passwords based on user specific criteria.

# Algorithm
# Import string
# and random libraries
# Ask user for the password length, 
# inclusion of special characters, 
# or numbers
# randomly generate password based on the length inputed
# concantenate the numbers, strings , and punctuation characters

import random
import string as char

print("Welcome to zen random password generator")
user_input = int(input("Enter your specfied length: "))

chars = char.ascii_letters + char.punctuation + char.digits

generated_password = ""

for _ in range (user_input):
    password = random.choice(chars)
    generated_password += password

print("Generated password of length ", user_input ,  ":", generated_password)