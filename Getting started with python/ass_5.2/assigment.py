largest = None
smallest = None

while True:
    num = input('Enter a number: ')

    if num == 'done':
        break

    # checking the input is valid or not valid
    try:
        number = int(num)
    except:
        print('Invalid input')
        continue

    # check largest number
    if largest is None:
        largest = number
    elif number > largest:
        largest = number

    # checking smallest number
    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number

print('Maximum is', largest)
print('Minimum is', smallest)
