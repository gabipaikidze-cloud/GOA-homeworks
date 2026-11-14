# დავალება 1

numbers = [5, 12, 15, 8, 20, 7, 25, 30, 11, 40]

result = set()

for num in numbers:
    if num % 5 == 0:
        print(num)
        result.add(num)

print("Set:", result)


# დავალება 2

animals = ("ძაღლი", "კატა", "ლომი", "ვეფხვი", "დათვი", "მგელი")

animal_list = []

i = 0

while i < len(animals):
    print(animals[i])
    animal_list.append(animals[i])
    i += 1

print("ცხოველების სია:", animal_list)


# დავალება 3

names = set()

for i in range(7):
    name = input("შეიყვანე ადამიანის სახელი: ")
    names.add(name)

print("სახელები:", names)
print("სახელების რაოდენობა:", len(names))


# დავალება 4

numbers = [-5, 10, -3, 7, -8, 12, 0, -2, 15, -10, 4, -1]

positive_numbers = []

i = 0

while i < len(numbers):
    if numbers[i] < 0:
        print(numbers[i])
    elif numbers[i] > 0:
        positive_numbers.append(numbers[i])

    i += 1

positive_tuple = tuple(positive_numbers)

print("დადებითი რიცხვების Tuple:", positive_tuple)


# დავალება 5

subjects1 = {"მათემატიკა", "ქართული", "ინგლისური", "ისტორია", "ფიზიკა"}

subjects2 = {"მათემატიკა", "ბიოლოგია", "ინგლისური", "ქიმია", "გეოგრაფია"}

for subject in subjects1:
    print(subject)

print("გაერთიანება:", subjects1.union(subjects2))

print("საერთო საგნები:", subjects1.intersection(subjects2))