class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.floors = number_of_floors
    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if 1 <= new_floor <= self.floors:
                print(f'Номер этажа {i}')
            else:
                print('Такого этажа не существует')
                break


a = House('ЖК Эльбрус', 30)
b = House('НикитаЛэнд', 100)
a.go_to(10)
print('')
b.go_to(99) 
