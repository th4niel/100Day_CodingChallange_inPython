class Parent:
    def __init__(self, fName, lName, age, occupation):
        self.firstName = fName
        self.lastName = lName
        self.yearsold = age
        self.job = occupation

    def printResult(self):
        print(self.firstName, self.lastName, self.yearsold)


class Children(Parent):
    def __init__(self, fName, lName, age, occupation, hobby):
        super().__init__(fName, lName, age, occupation)
        self.hobby = hobby

    def Combine(self):
        print("Hello, I am", self.firstName, self.lastName, self.yearsold,"years old","My hobby is", self.hobby)


child1 = Children("Yoruko", "Mitsuha", 15, "student", "Playing Game")
parent1 = Parent("Yoruko", "Kariba", 55, "CEO" )

child1.Combine()
parent1.printResult()