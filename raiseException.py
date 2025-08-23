height = float(input("Please enter your hight: "))
weight = int(input("Please enter your weight: "))



if height < 100 or weight < 29:
    raise ValueError("Are you even a human??")

bmi = weight/height **2
print(bmi)