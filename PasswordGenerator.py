"""
First asks the user if they want to generate a password then proceeds based on user input
"""

import string
import random

def generate_password():
    """
    Starts generating a random password based on user input
    """
    characters = list(string.ascii_letters + string.digits + string.punctuation)
    
    while True:
        try: 
            length = int(input("How long would you like your password to be? ").strip())
            break
        except ValueError:
            print("That was not a valid number. Please try again.")
    
    remove = input("Please name any letters or characters not allowed in the password. ").strip()
    for letter in remove:
        characters.remove(letter)
    random.shuffle(characters)
    
    password = ""
    for num in range(length):
        password += characters[num]
    print(password)

#Starts the program
accepted_answers = ["y","n","yes","no"]
accepted_yes = ["y","yes"]

while True:
    answer = input("Would you like to generate a password (Y/N)? ").strip().lower()
    if answer not in accepted_answers:
        print("Please enter a valid answer. Try again. ")
        continue
    else:
        if answer in accepted_yes:
            generate_password()
            break
        else:
            break
