student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# sum = 0
# for score in student_scores:
#     sum += score
#     print(sum)

# for score in student_scores:
#     if score == 199:
#         print(f"Yes this is the score you wanted! {score}")
#     else:
#         print(f"{score} is not the number you wanted!")

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)


