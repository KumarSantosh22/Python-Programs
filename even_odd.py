def even_odd(num):
    if num%2==0:
        return True
    return False


if __name__ == '__main__':
    num = int(input('Enter a number to check whether it is even or odd :  '))
    if even_odd(num):
        print(f'{num} is Even')
    else:
        print(f'{num} is Odd')
