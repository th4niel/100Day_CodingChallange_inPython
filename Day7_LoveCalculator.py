def calculate_love_score(name1, name2):
    true_counter = 0
    love_counter = 0

    combined_name = (name1 + name2).lower()

    for char in combined_name:
        if char in "true":
            true_counter += 1
        if char in "love":
            love_counter += 1

    print(f"Your Love Score is {str(true_counter)}{str(love_counter)}")

calculate_love_score("AliceDawson", "BobCarlsten")
