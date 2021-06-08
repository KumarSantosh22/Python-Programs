def factorial(num):
    fact = 1
    for i in range(1, (num) + 1):
        fact *= i
    return fact


if __name__ == '__main__':
    num = int(input("Enter a number to get the factorial : "))
    
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif (num) == 0:
        print("The factorial of 0 is 1")
    else:
        print(f'The factorial of {num} is  {factorial(num)}.')
