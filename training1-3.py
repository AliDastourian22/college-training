#-------------------Question1-------------------
""""
import datetime

birthdate = input("Enter your birthdate (YYYY-MM-DD): ")

birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d")

today = datetime.datetime.today()

age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

print("Your current age is:", age)
"""
#-------------------Question2-------------------
"""
semester1 = int(input("Enter your first semester grade: "))

semester2 = int(input("Enter your first semester grade: "))

semester3 = int(input("Enter your first semester grade: "))

average = (semester1 + semester2 + semester3)/3

print("Your current average is: ", average)
"""
#-------------------Question3-------------------
"""
seconds = int(input("Enter time in seconds: "))

hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
"""
#-------------------Question3-------------------
"""
price = float(input("Enter the price of the product: "))

profit = price * 0.1

total_price = price + profit 

print("Profit Amount (10%): Rs.", profit) 
print("Price After Adding Profit: Rs.", total_price)
"""











