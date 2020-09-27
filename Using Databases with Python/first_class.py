class PartAnimal:
    x = 0
    def party(self):
        y = 1
        y += 1
        self.x = self.x + 1
        print('So far:', self.x)
        print('Y:', y, '\n')


an = PartAnimal()

an.party()
an.party()
an.party()
an.party()
an.party()

# print(type(an))
# print(dir(an))