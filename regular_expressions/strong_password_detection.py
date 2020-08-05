"""
I feel as if I could create a regex that checks for everything in one go except for
in chunks and with the nested 'if' statements as I've done. But it works 
for now so whatever.
"""

import re

def password_detection(password):
    
    # Regexes to check
    lower_check = re.compile(r'[a-z]+') # 1 or more lower case character
    upper_check = re.compile(r'[A-Z]+') # 1 or more upper case character
    digit_check = re.compile(r'[0-9]+') # 1 or more digit character
    length_check = re.compile(r'.{8,}') # 8 or more characters total
	
	# Corresponding match operators
    lower_detect = lower_check.search(password)
    upper_detect = upper_check.search(password)
    digit_detect = digit_check.search(password)
    length_detect = length_check.search(password)

    if lower_detect == None: # If there's no lower case letters
        print("Not a strong password.")
    else:
        if upper_detect == None: # If there's no upper case letters
            print("Not a strong password.")
        else:
            if digit_detect == None: # If there's no digits
                print("Not a strong password.")
            else:
                if length_detect == None: # If it's not 8 characters long
                    print("Not a strong password.")
                else:
                    print("That's a strong password.")


password = input("Enter a password: ")
password_detection(password)
