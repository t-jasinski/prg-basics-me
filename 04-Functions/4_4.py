###
# Calculates the sum of the digits in a number
#
def sum_digits(number):

    number = abs(number)
    str_num = str(number)

    a=0
    
    for digit in str_num:
        a += int(digit)

    return a

any_number = int(input('Enter number: '))
result = sum_digits(any_number)
print(f"The sum of the digits in the number {any_number}, is {result}")