
# 1) 1-დან 20-მდე, გამოტოვე ლუწი რიცხვები

for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)


# 2) 1-დან 45-მდე, გამოტოვე 3-ზე გამყოფი რიცხვები

for i in range(1, 46):
    if i % 3 == 0:
        continue
    print(i)


# 3) 10-დან 50-მდე, გამოტოვე 20, 30 და 40

for i in range(10, 51):
    if i == 20 or i == 30 or i == 40:
        continue
    print(i)


# 4) მომხმარებელს შეაყვანინე 5 რიცხვი
# უარყოფითი რიცხვები არ დაბეჭდო

for i in range(5):
    num = int(input("Enter a number: "))

    if num < 0:
        continue

    print(num)


# 5) 1-დან 100-მდე, გამოიტანე რიცხვები,
# რომლებიც 5-ზე არ იყოფა

for i in range(1, 101):
    if i % 5 == 0:
        continue
    print(i)
