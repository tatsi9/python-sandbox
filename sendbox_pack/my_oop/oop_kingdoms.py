class Animal:
    photosynthesis = False
    size = "any size animal"
    legs = 4

    def __init__(self, name):
        self.name = name
        print('(An animal {0} created)'.format(self.name))

    @staticmethod
    def move():
        print("moving")

    @staticmethod
    def eat():
        print("eating")

    @classmethod
    def create(cls):
        assert cls is Animal
        print(cls.legs)
        # d = cls("D")
        # # d = cls("factory test")
        # d.move()
        # return d

    def how_many_legs(self):
        print("I have ", self.legs, " legs")
        return None


class Plant:
    photosynthesis = True
    size = "any size plant"

    # @sataticmethod
    # def no_move():
    #     """
    #     это функция класса, а не метод
    #     чтобы объек его вызвал надо использовать @sataticmethod
    #     """
    #     print("moving")


class Fungae:
    pass


# d = Animal.create()


dog = Animal("Toby")
dog.legs = 6
dog.how_many_legs()

doif2 = Animal("ddw")
# doif2.how_many_legs()

Animal.legs = 434

assert dog.legs == 6
assert doif2.legs == 434

dog.eat()
