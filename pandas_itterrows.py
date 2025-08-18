student_dict = {
    "student": ["Edwin", "Nathaniel", "Dorothy"],
    "score": [80, 89, 83]
}

# for (key, value) in student_dict.items():
#     print(key)


import pandas

pandas_data_frame = pandas.DataFrame(student_dict)
# print(pandas_data_frame)

#Loop through rows  of a data frame
for (index, row) in pandas_data_frame.iterrows():
    if row.student == "Edwin":
        print(row.score)