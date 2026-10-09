# problem 1

student = {
    "name": "raju",
    "age": "22",
    "department": "EEE"
}

print(student["name"])
print(student["age"])
print(student["department"])

student["age"] = 25
print(student["age"])
print(student.get("phone"))

print("\n")
print(student.keys())
print(student.values())
print(student.items())
print(student.get("phone"))


# problem 2

user = {
    "name": "Lamim",
    "age": "21",
    "address": {"city": "Dhaka", "country": "bangladesh"}
}

print("\n")
print(user["address"]["city"])


# problem 3

users = [
    {"id": "23", "name": "kalam", "age": 24},
    {"id": "24", "name": "salam", "age": 25},
    {"id": "25", "name": "rahim", "age": 22}
]

print("\n")
print(users[0]["age"])
print(users[2]["name"])
print(users[1]["id"])