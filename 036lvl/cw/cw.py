# დავალება 1

numbers = [5, 12, 20, 8, 15, 3, 25, 10, 30, 12]

new_set = set()

for number in numbers:
    if number > 10:
        print(number)
        new_set.add(number)

print("ახალი Set:", new_set)


# დავალება 2

cities = ("Tbilisi", "Batumi", "Kutaisi", "Gori",
          "Rustavi", "Telavi", "Zugdidi")

i = 0

while i < len(cities):
    print(cities[i])
    i += 1


# დავალება 3

fruits = []

for i in range(5):
    fruit = input("შეიყვანე საყვარელი ხილი: ")
    fruits.append(fruit)

fruit_set = set()

for fruit in fruits:
    fruit_set.add(fruit)

print("უნიკალური ხილები:", fruit_set)


# დავალება 4

numbers = (12, 7, 20, 15, 8, 3, 14, 9)

odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        print("ლუწი რიცხვი:", number)
    else:
        odd_numbers.append(number)

print("კენტი რიცხვების სია:", odd_numbers)


# დავალება 5

numbers = set()

i = 0

while i < 5:
    number = int(input("შეიყვანე რიცხვი: "))
    numbers.add(number)
    i += 1

print("შეყვანილი რიცხვები:", numbers)