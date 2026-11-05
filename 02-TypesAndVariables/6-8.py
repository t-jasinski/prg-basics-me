###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter second letter: ')
first_letter_code = ord(first)
second_letter_code = ord(last)
number_of_letters = -(first_letter_code - second_letter_code)
print(f'Between {first} and {last} is {number_of_letters} letters')
