# this is the factorial challenge in python
def factorial(number):
    if number == 0 or number == 1:
        return 1
    factorial = number
    while number >= 2:
        factorial *= number - 1
        number -= 1
    
    return factorial

print(factorial(5))