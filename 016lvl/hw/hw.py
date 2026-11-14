
# 1) 1-დან 15-მდე, არ გამოიტანო 7

for i in range(1, 16):
    if i == 7:
        continue
    print(i)


# 2) 2-დან 30-მდე, გამოტოვე ლუწი რიცხვები

for i in range(2, 31):
    if i % 2 == 0:
        continue
    print(i)


# 3) შეაყვანინე 7 რიცხვი და გამოიტანე მხოლოდ დადებითი

for i in range(7):
    num = int(input("Enter a number: "))

    if num <= 0:
        continue

    print(num)


# 4) 1-დან 40-მდე, გამოტოვე 4-ზე გამყოფი რიცხვები

for i in range(1, 41):
    if i % 4 == 0:
        continue
    print(i)


# 5) შეაყვანინე 10 რიცხვი, თუ 0 არის არ გამოიტანო

for i in range(10):
    num = int(input("Enter a number: "))

    if num == 0:
        continue

    print(num)


# 6) 1-დან 25-მდე, გამოტოვე 10-დან 15-მდე

for i in range(1, 26):
    if i >= 10 and i <= 15:
        continue
    print(i)


# 7) 5-დან 50-მდე, გამოტოვე 7-ზე გამყოფი რიცხვები

for i in range(5, 51):
    if i % 7 == 0:
        continue
    print(i)


# 8) შეაყვანინე 5 რიცხვი, თუ 10-ზე მეტია არ გამოიტანო

for i in range(5):
    num = int(input("Enter a number: "))

    if num > 10:
        continue

    print(num)
