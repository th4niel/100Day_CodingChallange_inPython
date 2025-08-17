import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# print(data["temp"].mean())

# #using attribute instead of string
# print(data.temp.max())

# print(data[data.condition == "Sunny"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32 
# print(f"{monday_temp_F} Fahrenheit")


#Create a dataFrame from scratch
data_dict = {
    "students": ["Edwin", "Nathaniel", "Jamy"],
    "scores": [99, 95, 85]
}

df = pandas.DataFrame(data_dict)
df.to_csv("try_csv.csv")