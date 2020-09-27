class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, name):
        self.name = name
        print('Name:', self.name)

    def party(self):
        self.x = self.x + 1
        print(self.name, 'Party count', self.x)


person1 = PartyAnimal('Amjed')
person1.party()
print('\n')

person2 = PartyAnimal('Danwand')
person2.party()
