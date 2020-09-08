text = "X-DSPAM-Confidence:    0.8475";

number_position = int(text.find('0'))
numbers = float(text[number_position:])

print(numbers)

