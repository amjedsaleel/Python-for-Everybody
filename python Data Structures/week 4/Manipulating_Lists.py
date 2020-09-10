a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

c = a + b
print(c)


# slicing
print('')
print(c[:])
print(c[2:])
print(c[:5])


# Building a list from scratch
print('')
stuff = list()
print(type(list))

stuff.append('Car')
stuff.append('Book')
stuff.append(2)
stuff.append('amjed')
print(stuff)

stuff.pop(3)
print(stuff)

stuff.insert(1, 'Shamil')
print(stuff)


# sorting
print('')
sample = [2, 5, 9, 1, 31]
sample.sort()
print(sample)

sample_2 = ['z', 'd', 'a', 'e', 'x', 'y']
sample_2.sort()
print(sample_2)