                                      # 1. 1-დან 20-მდე რიცხვები, მაგრამ 10-ზე ციკლი გაჩერდეს
i = 1

while i <= 20:
    if i == 10:
        break
    print(i)
    i += 1


# 2. 1-დან 50-მდე ყველა რიცხვის ჯამი
total = 0
i = 1

while i <= 50:
    total += i
    i += 1

print(total)


# 3. მომხმარებელს შეაქვს რიცხვები. 0-ის შეყვანისას ციკლი ჩერდება
total = 0

while True:
    num = int(input("შეიყვანე რიცხვი: "))

    if num == 0:
        break

    total += num

print(total)


# 4. 1-დან 200-მდე ყველა კენტი რიცხვის ჯამი
sum = 0
i = 1

while i <= 200:
    if i % 2 != 0:
        sum += i
    i += 1

print(sum)