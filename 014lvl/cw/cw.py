# 1. 1-დან 20-მდე მხოლოდ ლუწი რიცხვები
for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# 2. 5-დან 50-მდე რიცხვები, რომლებიც იყოფა 5-ზე
for i in range(5, 51):
    if i % 5 == 0:
        print(i)


# 3. მომხმარებელს შემოატანინე რიცხვი და გამოიტანე 1-დან ამ რიცხვამდე
num = int(input("შეიყვანე რიცხვი: "))

for i in range(1, num + 1):
    print(i)


# 4. რიცხვის გამრავლების ტაბულა 1-დან 10-მდე
num = int(input("შეიყვანე რიცხვი: "))

for i in range(1, 11):
    print(num, "*", i, "=", num * i)


# 5. 1-დან 100-მდე რიცხვების ჯამი
total = 0

for i in range(1, 101):
    total += i

print(total)