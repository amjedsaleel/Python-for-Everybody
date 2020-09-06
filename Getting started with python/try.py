input_value = input('Enter number: ')
try:
    number = int(input_value)
except:
    number = -1

if number >= 0:
    print("Good work")
else:
    print('Enter number in digits')
