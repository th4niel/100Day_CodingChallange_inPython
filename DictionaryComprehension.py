import random

names_list = ["Edwin", "Nathaniel", "Giantoro", "Abbhie", "Dorothy", "Domo", "Krie"]

student_score = {student:random.randint(1, 100) for student in names_list}

passed_student = {student:score for(student, score) in student_score.items() if score >= 60}
print(passed_student)


# new_dict = { new_key:new_value for item in list}
# use_exisisting_dict = { new-key:new_value for(key, value) in existing_dict.items()}