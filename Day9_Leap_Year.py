"""
1 - on every year that is divisible by 4 with no remainder
2 - EXCEPT every year that is evenly divisible by 100 with no remainder  
3 - UNLESS the year is also divisible by 400 with no remainder   

Points 2 will be shown as false when the user tries to check the year 2100

 e.g. The year 2000: 
2000 ÷ 4 = 500 (Leap)  
2000 ÷ 100 = 20 (Not Leap)  
2000 ÷ 400 = 5 (Leap!)  
 So the year 2000 is a leap year. 

 But the year 2100 is not a leap year because: 
 2100 ÷ 4 = 525 (Leap)  
 2100 ÷ 100 = 21 (Not Leap)  
 2100 ÷ 400 = 5.25 (Not Leap)  

"""

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True 
    elif year % 400 == 0:
        return True
    else:
        return False
    
print(is_leap_year(int(input("Please input the Leap year you want to check: "))))