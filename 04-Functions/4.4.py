###
# Calculates the sum of the digits in a number
#

def sum_digits(number):
    suma=0
    while number > 0:
        suma+= number%10
        number//10

    return suma
any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')