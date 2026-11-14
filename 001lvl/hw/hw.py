# level 18:

# 1. Nested for loop-ის გამოყენებით დაბეჭდეთ 3x3 ვარსკვლავების კვადრატი.

# 2. Nested while loop-ის გამოყენებით დაბეჭდეთ 4 სტრიქონი, თითოეულში 5 ვარსკვლავით.

# 3. Nested for loop-ის გამოყენებით დაბეჭდეთ ყველა შესაძლო წყვილი 1-დან 3-მდე რიცხვებით.

# 4. Nested while loop-ის გამოყენებით დაბეჭდეთ 1-დან 5-მდე რიცხვების გამრავლების ტაბულა.

# 5. Nested for loop-ის გამოყენებით შექმენით ვარსკვლავების სამკუთხედი.

# 6. Nested while loop-ის გამოყენებით შექმენით რიცხვების სამკუთხედი 1-დან 5-მდე.

# 7. Nested for loop-ის გამოყენებით შექმენით 5x5 კვადრატი, მაგრამ მესამე ვარსკვლავი არ დაბეჭდოთ. გამოიყენეთ continue.

# 8. მომხმარებელს შემოატანინეთ ორი რიცხვი და Nested while loop-ის გამოყენებით შექმენით ვარსკვლავების მართკუთხედი, სადაც პირველი რიცხვი იქნება სტრიქონების რაოდენობა, ხოლო მეორე — თითოეულ სტრიქონში ვარსკვლავების რაოდენობა.
# 1
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()


# 2
i = 0
while i < 4:
    j = 0
    while j < 5:
        print("*", end=" ")
        j += 1
    print()
    i += 1


# 3
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# 4
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print(i * j, end=" ")
        j += 1
    print()
    i += 1


# 5
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


# 6
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1


# 7
for i in range(5):
    for j in range(5):
        if j == 2:
            continue
        print("*", end=" ")
    print()


# 8
a = int(input("შეიყვანე სტრიქონების რაოდენობა: "))
b = int(input("შეიყვანე ვარსკვლავების რაოდენობა: "))

i = 0

while i < a:
    j = 0
    while j < b:
        print("*", end=" ")
        j += 1
    print()
    i += 1