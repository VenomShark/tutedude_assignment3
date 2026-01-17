def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)
    
input = int(input("Enter a number to calculate its factorial: "))
result = factorial(input)
print(f"The factorial of {input} is {result}")