class house:
    house_history = []

    def __new__(cls, *args, **kwargs):
        isinstance = super().__new__(cls)
        cls.house_history.append(args[0])
        return isinstance

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __del__(self):
         print(f"{self.name} снесен, но останется в истории")

h1 = house('ЖК Эльбрус', 10)
print(house.house_history)
h2 = house('ЖК Акация', 20)
print(house.house_history)
h3 = house('ЖК Матрёшки', 20)
print(house.house_history)

# Удаление объектов
del h2
del h3

print(house.house_history)
