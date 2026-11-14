# დავალება 1
fruits1 = {"apple", "banana", "orange", "kiwi", "mango"}
fruits2 = {"grape", "watermelon", "apple", "peach", "cherry"}

all_fruits = fruits1.union(fruits2)

print(all_fruits)


# დავალება 2
numbers1 = {10, 20, 30, 40, 50}
numbers2 = {30, 40, 50, 60, 70}

common_numbers = numbers1.intersection(numbers2)

print(common_numbers)


# დავალება 3
students1 = {"Giorgi", "Nika", "Luka", "Ana"}
students2 = {"Mariam", "Saba", "Giorgi", "Nika"}

all_students = students1.union(students2)

print(all_students)
print(len(all_students))


# დავალება 4
colors1 = {"red", "green", "blue", "yellow"}
colors2 = {"blue", "yellow", "black", "white"}

common_colors = colors1.intersection(colors2)

print(common_colors)


# დავალება 5
python_students = {"Giorgi", "Nika", "Ana", "Luka"}
javascript_students = {"Nika", "Mariam", "Giorgi", "Saba"}
react_students = {"Ana", "Saba", "Luka", "Mariam"}

# ყველა უნიკალური მოსწავლე
all_students = python_students.union(javascript_students).union(react_students)

# მოსწავლეები, რომლებიც Python-ს და JavaScript-ს სწავლობენ
common_students = python_students.intersection(javascript_students)

print("ყველა მოსწავლე:", all_students)
print("Python-ისა და JavaScript-ის მოსწავლეები:", common_students)