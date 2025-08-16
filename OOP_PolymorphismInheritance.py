class Parenting:
    def __init__(self, fName, lName):
        self.firstName = fName
        self.lastName = lName

    def randomMethod():
        pass


class Child1(Parenting): #polymorphism
    def learn(self): #Inheritance
        print("Everyday learn math")


class Child2(Parenting):
    def learn(self):
        print("Everyday Learn Physic")


child1 = Child1("Yomo", "Matsusaki")
child2 = Child2("Itsuka", "Renbo")


for x in (child1, child2):
    print(x.firstName, x.lastName)
    x.learn()