class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (f"Nieruchomości: {self.address}\n"
                f"Powierzchnia: {self.area} m2, "
                f"Liczba pokoi: {self.rooms}, "
                f"cena: {self.price} zł")


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"Dom:\n{super().__str__()}\n"
                f"Wielkość działki: {self.plot} m2")


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Mieszkanie:\n{super().__str__()}\n"
                f"Piętro: {self.floor}")


house1 = House(area=200,
               rooms=7,
               price=850000,
               address="Katowice, ul. Podlaska 1",
               plot=700)
flat1 = Flat(area=70,
             rooms=4,
             price=380000,
             address="Tychy, ul. Nad wodą 1",
             floor=2)

print(house1)
print()
print(flat1)
