# 1) Tuple და პირველი და ბოლო ელემენტი
colors = ("red", "green", "blue", "yellow")

print(colors[0])
print(colors[-1])


# 2) Tuple-ის სიგრძე
numbers = (10, 20, 30, 40, 50, 60)

print(len(numbers))


# 3) Unpacking
point = (10, 20, 30)

x, y, z = point

print(x)
print(y)
print(z)


# 4) User Info და Unpacking
user_info = ("გიორგი", 25, "თბილისი")

name, age, city = user_info

print(name)
print(age)
print(city)


# 5) count() და index()
numbers2 = (1, 5, 3, 5, 2, 5, 8, 4)

print(numbers2.count(5))
print(numbers2.index(3))