#forest class
class Animal:

    nameproperty = ""
    foodproperty = ""

    def __init__(self, name, food):
        self.nameproperty = name
        self.__foodproperty = food

    def getname(self):
        return self.name

    def getfood(self):
        return self.food

Animalnew = Animal("lion","meat")

Animaltwo = Animal("Hyena","Leftovers")

print(Animalnew.nameproperty, Animalnew.foodproperty)
print(Animaltwo.nameproperty, Animaltwo.foodproperty)


