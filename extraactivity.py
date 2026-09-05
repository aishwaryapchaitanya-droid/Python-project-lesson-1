class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price 

    def setprice(self, newprice):
        self.__price = newprice

    def __str__(self):
        return self.name + " - $" + str(self.__price)

item = Product("Chocolate", 50)

print(item)
item.__price = 100

print("\nAfter direct change: ")
print(item)

item.setprice(100)

print("\nAfter using setter: ")
print(item)