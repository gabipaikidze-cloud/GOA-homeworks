
# 1) Nested Loop - 3x3 ვარსკვლავების კვადრატი

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()


# 2) 3 სტრიქონი, თითოეულში რიცხვები 1-დან 4-მდე

for i in range(3):
    for j in range(1, 5):
        print(j, end=" ")
    print()


# 3) გამრავლების ტაბულა 1-დან 3-მდე

for i in range(1, 4):
    for j in range(1, 4):
        print(i, "x", j, "=", i * j)
