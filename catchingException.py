# try:
#     with open("file.txt") as data_file:
#         data_file.read()
# except:
#     print("There is no such file or directory")

# else:
#     print("You succeed !")



try:
    file = open("file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("hello world!")
except KeyError as key_error:
    print(f"there is no {key_error}")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")