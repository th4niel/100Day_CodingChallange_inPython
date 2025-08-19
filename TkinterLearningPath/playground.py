# def add(*ganteng): #*args  == return tuple as the result
#     print(ganteng[1])
#     sum = 0
#     for x in ganteng:
#         sum += x
#     return sum

# print(add(2, 5, 6, 8, 10))


# def add(x, b, **kwargs): #kwargs == return dictionary (key:value) as the result
#     # print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     x *= kwargs["num1"]
#     b += kwargs["num2"]
#     print(x)
#     print(b)


# add(3, 5,   num1 = 2,num2 = 3)


#kwargs OOP example

class Car:

    def __init__(self, **kw):
        self.model = kw["model"]
        self.year = kw.get("year") #get() method to catch error whenever there is no argument in the object


edwin_car = Car(model= "Honda")
print(edwin_car.model, edwin_car.year)


