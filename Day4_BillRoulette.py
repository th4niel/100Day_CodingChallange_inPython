import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# random_gen = random.choice(friends)
#
# print(f"Congratulation, you are choosen one Mr/mrs '{random_gen}' to pay Our Bills")


random_gen = random.randint(0,4)
choose_friend = friends[random_gen]

print(f"Congratulation Mr/Mrs '{choose_friend}' to pay Our Bills")