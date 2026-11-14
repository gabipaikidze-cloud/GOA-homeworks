# 1. 1-დან 100-მდე ყველა რიცხვის ჯამი
total = 0
i = 1

while i <= 100:
    total += i
    i += 1

print(total)


# 2. 1-დან 100-მდე ყველა კენტი რიცხვის ჯამი
total = 0
i = 1

while i <= 100:
    if i % 2 != 0:
        total += i
    i += 1

print(total)


# 3. 1-დან 50-მდე რიცხვები, 25-ზე ციკლი გაჩერდეს
i = 1

while i <= 50:
    if i == 25:
        break

    print(i)
    i += 1


# 4. რიცხვების შეყვანა, 0-ის შემთხვევაში ციკლი გაჩერდეს
total = 0

while True:
    num = int(input("შეიყვანე რიცხვი: "))

    if num == 0:
        break

    total += num

print(total)


# 5. 1-დან n-მდე ყველა ლუწი რიცხვის ჯამი
n = int(input("შეიყვანე n: "))

total = 0
i = 1

while i <= n:
    if i % 2 == 0:
        total += i

    i += 1

print(total)


# 6. უარყოფითი რიცხვის შემთხვევაში ციკლი გაჩერდეს
total = 0

while True:
    num = int(input("შეიყვანე რიცხვი: "))

    if num < 0:
        break

    total += num

print(total)


# 7. 0-ზე გაჩერდეს, უარყოფითი რიცხვები გამოტოვოს
total = 0

while True:
    num = int(input("შეიყვანე რიცხვი: "))

    if num == 0:
        break

    if num < 0:
        continue

    total += num

print(total)