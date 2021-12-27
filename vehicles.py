from abc import abstractmethod, ABCMeta

class Vehicle(object, metaclass=ABCMeta):
    def __init__(self,eng_type,brand,break_type,colour):
        self.eng_type = eng_type
        self.brand = brand
        self.break_type = break_type
        self.colour = colour


class Car(Vehicle):
    def __init__(self, eng_type, brand, break_type, colour):

        print("__init__car")
        super().__init__(eng_type, brand, break_type, colour)




if __name__ == "__main__":
    c1 = Car("petrol","Honda","disk","white")
    print(c1)
    # v =Vehicle("petrol","Honda","disk","white")
    # print(v)