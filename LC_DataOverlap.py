# Data Overlap
# 💪 This exercise is HARD 💪 
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 
# You are going to create a list called result which contains the numbers that are common in both files. 
# e.g. if file1.txt contained: 
# 1 
# 2 
# 3
# and file2.txt contained: 
# 2
# 3
# 4
# result = [2, 3]
# IMPORTANT:  The output should be a list of integers and not strings!
# Try to use List Comprehension instead of a Loop. 


with open("file1.txt") as f1, open("file2.txt") as f2:
    file1 = [int(item.strip()) for item in f1.readlines()]
    file2 = [int(item.strip()) for item in f2.readlines()]

result = [x for x in file1 if x in file2]
print(result)