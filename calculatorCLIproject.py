print('Welcome to the tip Calculator!')
bill = float(input("What was the total bill?"))
tip =  int(input("How much tip would you like to give? 10, 12, or 15 ?"))
split = int(input("How many people to split the bill?"))

tip_as_percent = tip/100
total_bill = bill * tip_as_percent + bill
final_result = total_bill/split

print(f"Each Person should pay: {final_result:.2f}")