#! python3

# Write a function that takes a string and does the same thing
# as the 'strip()' string method.

import re

def regex_strip(string, char_to_remove=None):
    stripping_regex = re.compile(f'{char_to_remove}')

    # TODO: Set up the regex basics

    # TODO: Check to see if the string has any matches (if applicable)

    # TODO: Remove the chars to be removed, as well as whitespace if nothing is provided


choice = input("Please enter a string: ")
to_remove = input("Please enter which chars to remove: ")

if to_remove == '':
    regex_strip(choice)
else:
    regex_strip(choice, to_remove)