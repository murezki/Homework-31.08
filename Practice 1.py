# Примитивные типы данных в Python:
age = 15
print(age)

# Не примитивные типы данных:
friends_list = ("Yabadaba", "Hasbulla", "Agaraguzhu")
print(friends_list)

# Условные конструкции:
def ager(age):
    if age >= 18:
        print("Вы совершеннолетний")
    else:
        print("Вы несовершеннолетний")
ager(age)

# Циклы for:
for name in friends_list:
    print(f"Привет, {name}!")

# Циклы while:
while age < 30:
    print("возраст:", age)
    age += 1

# Возвратные функции:
number1 = 420
number2 = 69
def add_numbers(a, b):
    return a + b
result = add_numbers(number1, number2)
print(result)

# Невозвратные функции:
name = "расул"
def print_greeting(name):
    print(f"салам, {name}")
print_greeting(name)

# Рекурсия:
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)
result2 = factorial(4)
print(result2)