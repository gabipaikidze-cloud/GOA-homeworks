# 1) Tuple, len() და in
numbers = (10, 20, 30, 40, 50, 60)

print(len(numbers))
print(30 in numbers)


# 2) Set, add() და discard()
fruits = {"apple", "banana", "orange", "mango", "grape"}

fruits.add("kiwi")
fruits.discard("banana")

print(fruits)


# 3) Tuple, in და len()
animals = ("dog", "cat", "lion", "tiger", "bear")

print("lion" in animals)
print(len(animals))


# 4) Set, remove(), add() და in
numbers = {10, 20, 30, 40, 50, 60}

numbers.remove(30)
numbers.add(70)

print(70 in numbers)
print(numbers)


# 5) Set, len(), discard() და in
languages = {"Python", "Java", "C++", "JavaScript"}

print(len(languages))

languages.discard("PHP")

print("Python" in languages)
print(languages)