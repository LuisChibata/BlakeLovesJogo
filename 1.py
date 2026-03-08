import my_api

def identity(name, age):
    print(f"your name is {name} and your age is {age}")
identity("Blake", 17)

def sum(num1, num2):
    print(num1+num2)
sum(1, 5)

print(my_api.add(1, 9))