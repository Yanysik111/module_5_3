
class Building:
    def __init__(self, name, numberOfFloors, buildingType ):
        self.name = name
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

h1 = Building('ЖК Горский', 18, 'кирпичное' )
h2 = Building('Домик в деревне', 2, 'бревенчатое')
print(h1 == h2)
