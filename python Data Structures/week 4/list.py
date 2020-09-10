name = ['Amjed', 'Danwand', 'Shamil']
print(type(name))

for i in name:
    print('Happy new year:', i)

print('')
for i in range(len(name)):
    friend = name[i]
    print('Happy new hear:', friend)

print('')
for i in range(len(name)):
    friend = name[i+2]
    print(friend)
    break
