# 1. 1-დან 100-მდე ყველა ლუწი რიცხვის ჯამი
total = 0

for i in range(1, 101):
    if i % 2 == 0:
        total += i

print(total)


# 2. 1-დან მომხმარებლის მიერ შეყვანილ რიცხვამდე
# რამდენი რიცხვია ისეთი, რომელიც 3-ზე იყოფა
num = int(input("შეიყვანე რიცხვი: "))
count = 0

for i in range(1, num + 1):
    if i % 3 == 0:
        count += 1

print(count)


# 3. მომხმარებელს შემოატანინე 5 რიცხვი და იპოვე მათი ჯამი
total = 0

for i in range(5):
    num = int(input("შეიყვანე რიცხვი: "))
    total += num

print(total)


# 4. მომხმარებელს შემოატანინე 5 რიცხვი და იპოვე ყველაზე დიდი
largest = None

for i in range(5):
    num = int(input("შეიყვანე რიცხვი: "))

    if largest is None or num > largest:
        largest = num

print(largest)


# 5. მომხმარებელს შემოატანინე სიტყვა და გამოიტანე თითოეული ასო ცალ-ცალკე
word = input("შეიყვანე სიტყვა: ")

for letter in word:
    print(letter)