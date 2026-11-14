# Level 06


# 1) შექმენი ორი ცვლადი, სადაც მომხმარებელს შემოატანინებ ორ რიცხვს.
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")


# 2) პირველ დავალებაში შექმნილი ორივე ცვლადი გადაიყვანე ინტეჯერად (int()).
num1 = int(num1)
num2 = int(num2)


# 3) დაბეჭდე ამ ორ რიცხვზე ყველა მათემატიკური მოქმედების შედეგი:
# (+, -, *, /, %, //, **)
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)
print(num1 // num2)
print(num1 ** num2)


# 4) შექმენი ცვლადი, სადაც მომხმარებელს შემოატანინებ თავის სახელს.
name = input("Enter your name: ")


# 5) შექმენი ცვლადი, სადაც მომხმარებელს შემოატანინებ თავის ასაკს.
age = input("Enter your age: ")


# 6) f-string-ის გამოყენებით დაბეჭდე:
# "Hello, my name is {სახელი} and I am {ასაკი} years old."
print(f"Hello, my name is {name} and I am {age} years old.")


# 7) მომხმარებელს შემოატანინე თავისი საყვარელი ფერი
# და f-string-ის გამოყენებით დაბეჭდე:
# "My favorite color is {ფერი}."
color = input("Enter your favorite color: ")

print(f"My favorite color is {color}.")


# 8) მომხმარებელს შემოატანინე ორი რიცხვი,
# გადაიყვანე ინტეჯერებად და დაბეჭდე მათი ჯამი, სხვაობა და ნამრავლი.
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

print(number1 + number2)
print(number1 - number2)
print(number1 * number2)


# 9) მომხმარებელს შემოატანინე სახელი, გვარი და ქვეყანა.
# f-string-ის გამოყენებით დაბეჭდე:
# "My name is {სახელი} {გვარი} and I live in {ქვეყანა}."
first_name = input("Enter your name: ")
last_name = input("Enter your surname: ")
country = input("Enter your country: ")

print(f"My name is {first_name} {last_name} and I live in {country}.")


# 10) მომხმარებელს შემოატანინე ორი რიცხვი,
# გადაიყვანე ინტეჯერებად და დაბეჭდე:
# პირველი რიცხვი მეორე ხარისხში.
# მეორე რიცხვი მესამე ხარისხში.
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

print(number1 ** 2)
print(number2 ** 3)
