number_list = list()
while True:
    inp = input('Enter number:')
    if inp == 'done':
        break
    value = float(inp)
    number_list.append(value)
average = sum(number_list) / len(number_list)
print(average)