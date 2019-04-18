# Gudni Natan Gunnarsson
# 31.01.2019

# Part 2


def sum_of_odd(x: int, y: int) -> int:
    if x >= y:
        return (x % 2) * x
    return (x % 2) * x + sum_of_odd(x + 1, y)


def raise_by_one(lis: list):
    if not lis:
        return
    item = lis.pop() + 1
    raise_by_one(lis)
    lis.append(item)


# Part 3
class ArrayList(object):
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0

    def prepend(self, value):
        if self.size >= self.capacity:
            self._resize()
        else:
            for i in range(self.size, 0, -1):
                self.arr[i] = self.arr[i - 1]
        self.arr[0] = value
        self.size += 1

    def set_at(self, index, value):
        if 0 <= index < self.size:
            self.arr[index] = value

    def get_size(self):
        return self.size

    def print_list(self):
        string = str()
        for i in range(self.size - 1):
            string += str(self.arr[i]) + " "
        if self.size:  # No extra space at the end
            string += str(self.arr[self.size - 1])
        print(string)

    def _resize(self):
        self.capacity *= 2
        new_arr = [None] * self.capacity
        for i in range(self.capacity // 2):
            new_arr[i + 1] = self.arr[i]
        self.arr = new_arr


# Part 4
class Car(object):
    def __init__(self, plate_nr: str, brand: str, passenger_count: int):
        self.__plate_nr = plate_nr
        self.__brand = brand
        self.__passenger_count = passenger_count

    def get_plate_nr(self) -> str:
        return self.__plate_nr

    def get_brand(self) -> str:
        return self.__brand

    def get_passenger_count(self) -> int:
        return self.__passenger_count

    def set_plate_nr(self, plate_nr: str):
        self.__plate_nr = plate_nr

    def set_brand(self, brand: str):
        self.__brand = brand

    def set_passenger_count(self, count: int):
        self.__passenger_count = count

    def __str__(self):
        return '{}: {}, {} passengers'.format(
            str(self.__plate_nr),
            str(self.__brand),
            str(self.__passenger_count),
        )


class Rental(object):
    def __init__(self):
        self.cars = dict()

    def add_car(self, plate_nr: str, brand: str, passenger_count: int):
        a_car = Car(plate_nr, brand, passenger_count)
        self.cars[plate_nr] = a_car

    def get_car(self, plate_nr: str) -> (Car, None):
        return self.cars.get(plate_nr, None)

    def change_brand(self, plate_nr: str, new_brand: str):
        try:
            self.cars[plate_nr].set_brand(new_brand)
        except KeyError:
            return

    def change_passenger_count(self, plate_nr: str, count: int):
        try:
            self.cars[plate_nr].set_passenger_count(count)
        except KeyError:
            return

    def __str__(self):
        car_strings = [str(a_car) for a_car in self.cars.values()]
        return "\n".join(car_strings)
