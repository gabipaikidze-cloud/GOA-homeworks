# Level 07


# 1) მომხმარებელს შემოატანინე თავისი ასაკი და რიცხვი 18-თან შეადარე
# ოპერატორების (>, <, >=, <=, !=, ==) გამოყენებით.
# თითოეული შედარების შედეგი ცალ-ცალკე დაბეჭდე.

age = int(input("Enter your age: "))

print(age > 18)
print(age < 18)
print(age >= 18)
print(age <= 18)
print(age != 18)
print(age == 18)


# 2) მომხმარებელს შემოატანინე ორი რიცხვი
# და ყველა ნასწავლი შედარების ოპერატორის გამოყენებით შეადარე ისინი ერთმანეთს.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 != num2)
print(num1 == num2)


# 3) შექმენი ორი ცვლადი, რომლებშიც შეინახავ ორ სხვადასხვა ტემპერატურას.
# შეადარე ისინი ოპერატორების (>, <, >=, <=, !=, ==) გამოყენებით.

temperature1 = 25
temperature2 = 30

print(temperature1 > temperature2)
print(temperature1 < temperature2)
print(temperature1 >= temperature2)
print(temperature1 <= temperature2)
print(temperature1 != temperature2)
print(temperature1 == temperature2)


# 4) შექმენი ორი ცვლადი, რომლებშიც შეინახავ ორ სხვადასხვა სტრინგს (სახელს)
# და შეამოწმე, ტოლი არიან თუ არა (==) და განსხვავდებიან თუ არა (!=).

name1 = "Nika"
name2 = "Giorgi"

print(name1 == name2)
print(name1 != name2)


# 5) შექმენი სამი ცვლადი სხვადასხვა რიცხვებით.
# ჯერ შეადარე პირველი და მეორე,
# შემდეგ მეორე და მესამე,
# ბოლოს პირველი და მესამე
# შედარების ოპერატორების (>, <, >=, <=, !=, ==) გამოყენებით.

a = 10
b = 20
c = 30

print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a != b)
print(a == b)

print(b > c)
print(b < c)
print(b >= c)
print(b <= c)
print(b != c)
print(b == c)

print(a > c)
print(a < c)
print(a >= c)
print(a <= c)
print(a != c)
print(a == c)
