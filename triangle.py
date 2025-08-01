height = 5

for x in range(1, height +1, +1 ):
    space = " " * (height - x)
    star = "*" * ( 2 * x -1)
    print(space + star)

for x in range(height -1,0, -1):
    space = " " * (height - x)
    star = "*" * (2*x -1)
    print(space + star)