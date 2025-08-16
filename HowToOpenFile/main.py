# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)


with open("my_file.txt", mode="a") as file: #mode a= append, w = write, r = read
    file.write("\nsaya ganteng banget")


    #write mode can be used to create a file