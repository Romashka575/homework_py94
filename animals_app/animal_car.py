class Moving:
    def move(self):
        raise NotImplementedError


class Animal(Moving):
    def voice(self):
        raise NotImplementedError


class Transport(Moving):
    def launch(self):
        raise NotImplementedError


class Duck(Animal):
    def voice(self):
        print("Krya")

    def move(self):
        print("Duck is swimming")


class Tiger(Animal):
    def voice(self):
        print("Rrrrr")

    def move(self):
        print("Tiger is running")


class Car(Transport):
    def __init__(self):
        self.status = "not started"

    def move(self):
        if self.status == "started":
            print("The car is moving")
        else:
            print("Please, start the car")

    def launch(self):
        self.status = "started"
        print("The car is started")


duck = Duck()
tiger = Tiger()
car = Car()
