
class Building:
    def __init__(self, numberOfFloors, buildingType ):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __str__(self):
        return f'{self.buildingType}'

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

h1 = Building( 18, 'кирпичное' )
h2 = Building( 2, 'бревенчатое')
print(h1 == h2)
