# 1) Tuple fruits
fruits = ("apple", "banana", "orange", "mango", "grape")

print(fruits[1])
print(fruits[3])


# 2) Tuple-ის სიგრძე
numbers1 = (15, 25, 35, 45, 55, 65, 75)

print(len(numbers1))


# 3) Unpacking
coordinates = (100, 200, 300)

a, b, c = coordinates

print(a)
print(b)
print(c)


# 4) Student Info
student_info = ("ნიკა", 17, "ბათუმი")

name, age, city = student_info

print(name)
print(age)
print(city)


# 5) count() და index()
numbers2 = (2, 4, 6, 4, 8, 4, 10, 6, 4)

print(numbers2.count(4))
print(numbers2.index(6))


# 6) Tuple animals
animals = ("dog", "cat", "lion", "tiger", "elephant", "bear")

print(animals[0])
print(animals[1])
print(animals[2])


# 7) უარყოფითი ინდექსები
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

print(days[-2])
print(days[-1])


# 8) count() და index()
scores = (90, 75, 90, 60, 85, 90, 70)

print(scores.count(90))
print(scores.index(75))


# 9) in ოპერატორი
languages = ("Python", "JavaScript", "Java", "C++")

print("Python" in languages)
print("PHP" in languages)


# 10) პირველი, შუა და ბოლო ელემენტი
numbers3 = (10, 20, 30, 40, 50)

print(numbers3[0])
print(numbers3[2])
print(numbers3[-1])


# 11) Unpacking
person = ("ანა", 16, "ქუთაისი", "Python")

name, age, city, language = person

print(name)
print(age)
print(city)
print(language)