# problem 1 

numbers = {12, 33, 21, 44, 67, 44, 45, 55, 56, 67}

print(numbers)
print(set(numbers))


# problem 2

a = {23, 11, 45, 32, 67, 89, 34}
b = {44, 45, 23, 56, 78, 89, 35, 66}

print("\n")
print("A: ", a)
print("B: ", b)

print("union: ", a | b)
print("intersection: ", a & b)
print("subtraction: ", a - b)
print("symmetry: ", a ^ b)