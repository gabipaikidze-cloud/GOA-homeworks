# დავალება 1
colors = ("red", "blue", "green", "yellow", "black", "white")

print(len(colors))
print("blue" in colors)


# დავალება 2
cities = {"Tbilisi", "Batumi", "Kutaisi", "Gori", "Rustavi"}

cities.add("Telavi")
cities.remove("Gori")

print(cities)


# დავალება 3
cars = ("BMW", "Mercedes", "Toyota", "Audi", "Honda")

print("BMW" in cars)
print(len(cars))


# დავალება 4
scores = {10, 20, 30, 40, 50, 60}

scores.discard(30)
scores.add(70)

print(70 in scores)


# დავალება 5
programming_languages = {"Python", "JavaScript", "Java", "C++", "HTML"}

print(len(programming_languages))

programming_languages.discard("PHP")

print("JavaScript" in programming_languages)
print(programming_languages)


# დავალება 6
numbers = (10, 20, 30, 40, 50, 60, 70)

print(50 in numbers)
print(len(numbers))


# დავალება 7
animals = {"dog", "cat", "lion", "tiger", "elephant", "bear"}

animals.remove("lion")
animals.add("wolf")
animals.discard("snake")

print(animals)


# დავალება 8
days = ("Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday")

print(len(days))
print("Sunday" in days)