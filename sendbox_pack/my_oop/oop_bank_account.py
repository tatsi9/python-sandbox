class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    # def print_public_data(self):
    #     print(self.name, self.balance, self.passport)

    # def print_protected_data(self):
    #     print(self._name, self._balance, self._passport)

    def print_public_data(self):
        print(self.__name, self.__balance, self.__passport)


my_acc = BankAccount("Ann", "10000", "AB5381027")

# print(my_acc.name)
# print(my_acc.balance)
# print(my_acc.passport)
# my_acc.print_public_data()

# print(my_acc._name)
# print(my_acc._balance)
# print(my_acc._passport)
# my_acc.print_protected_data()

# print(my_acc.__name) - ytkmpz
my_acc.print_public_data()
