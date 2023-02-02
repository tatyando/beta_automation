class Address:
    def __init__(self, index, city, street, building_number, flat_number):
        self.index = index
        self.city = city
        self.street = street
        self.building_number = building_number
        self.flat_number = flat_number
    
    def __str__(self):
        return self.index + " " + self.city + " " + self.street + " " + self.building_number + " " + self.flat_number

class Mailing():
    def __init__(self, to: Address, otkuda: Address, cost, track):
        self.to = to
        self.otkuda = otkuda
        self.cost = cost
        self.track = track
