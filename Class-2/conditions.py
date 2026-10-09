# problem 1

age = int(input("enter your age: "))
salary = float(input("enter your salary: "))

if age>= 18 and salary>=30000:
    print("eligible")

else:
    print("not eligible")



# problem 2

list = [45, 35, 23, 47, 35, 86, 25, 58, 23]

num = int(input("enter a number: "))

if num in list:
    print("number exists")

else:
    print("number doesn't exist")



# problem 3

student = {
    "name": "raju",
    "age": "22",
    "department": "EEE",
    "email": "user@email.com"
}

if student.get("email"):
    print("email exist")

else:
    print("email doesn't exist")



# problem 4

cart =[
    {"name": "keyboard", "price": "3400", "quantity": "3"},
    {"name": "mouse", "price": "1500", "quantity": "2"}
]

total=0

for item in cart:
    total += int(item ["price"]) * int(item ["quantity"])

if total>= 5000:
    discount= total * .10

else:
    discount = 0

print("Total: ", total)
print("Payable: ", total - discount)
