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
#------week3--------Question1-------------------
product_prices = []

for i in range(5):
    price = float(input(f"Enter price of product {i+1}: "))

    product_prices.append(price)

average_price = sum(product_prices)
print("The average price: Rial", average_price)

large_price=max(product_prices)

if large_price > 1000000:
    print("this is the biggest price; ", large_price)

sell_prices = []
for price in product_prices:
    sel_price = price * 0.1
    sell_prices.append(sel_price)
print("Sell Price is : ", sel_price)
#------week3--------Question2-------------------
age=[]
for i in range(10):
    ages = int(input("Enter age " + str(i+1) + " : "))
    age.append(ages)
age.remove(max(age))
age.remove(max(age))
age.remove(min(age))
age.remove(min(age))

average_age = sum(age) / len(age)
print("The average age is : ", average_age)

oldest_age = max(ages)
print("The oldest age is : ", oldest_age)
#------week3--------Question4-------------------
salaries = []

for i in range(12):
    salary = float(input("Enter salary for month " + str(i+1) + " : "))
    salaries.append(salary)
average_salary = sum(salaries) / 12
print("The average salary is : ", average_salary)

largest_salary = max(salaries)
print("The largest salary is : ", largest_salary)

task_payment = largest_salary * 0.15
print("The total task payment is : ", task_payment)







