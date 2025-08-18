# number = [1, 2, 3]
# new_list = [x * 3 for x in number]
# print(new_list)

# new_list = []
# for x in number:
#     add_new = x *3
#     new_list.append(add_new)
# print(new_list)

# new_list = [x*2 for x in range(1, 5)]
# print(new_list)


names_list = ["Edwin", "Nathaniel", "Giantoro", "Abbhie", "Dorothy", "Domo", "Krie"]

new_List = [x.upper() for x in names_list if len(x) >= 6]
print(new_List)