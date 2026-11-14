
# 1) Nested for loop - 3x3 ვარსკვლავების კვადრატი

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()


# 2) Nested while loop - 4 სტრიქონი, 5 ვარსკვლავით

i = 0

while i < 4:
    j = 0

    while j < 5:
        print("*", end=" ")
        j += 1

    print()
    i += 1


# 3) ყველა შესაძლო წყვილი 1-დან 3-მდე

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# 4) Nested while loop - გამრავლების ტაბულა 1-დან 5-მდე

i = 1

while i <= 5:
    j = 1

    while j <= 5:
        print(i, "x", j, "=", i * j)
        j += 1

    i += 1


# 5) ვარსკვლავების სამკუთხედი

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


# 6) Nested while loop - რიცხვების სამკუთხედი

i = 1

while i <= 5:
    j = 1

    while j <= i:
        print(j, end=" ")
        j += 1

    print()
    i += 1


# 7) 5x5 კვადრატი - მესამე ვარსკვლავი არ დაბეჭდო

for i in range(5):
    for j in range(5):
        if j == 2:
            continue
        print("*", end=" ")
    print()


# 8) მომხმარებლის რიცხვებით ვარსკვლავების მართკუთხედი

rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))

i = 0

while i < rows:
    j = 0

    while j < columns:
        print("*", end=" ")
        j += 1

    print()
    i += 1
