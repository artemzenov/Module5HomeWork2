class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if (new_floor <= self.number_of_floors and
            new_floor > 1):
            for num_floor in range(1, new_floor + 1):
                print(num_floor)
        else:
            print(f'Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, '
                f'кол-во этажей: {self.number_of_floors}')