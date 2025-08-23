x= lambda salary, work_hours: salary*work_hours


print(x(30000,8))


#lambda anonymous parameter 
def Myfunc(b):
    return lambda x: x*b #variable x is anonumous parameter

trytry = Myfunc(10)

print(trytry(2))