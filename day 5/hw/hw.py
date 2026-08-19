# Level 05


# 1. მომხმარებელს შეაყვანინე ასაკი, გადააქციე int-ად და დაბეჭდე შედეგი.
age = int(input("Enter your age: "))
print(age)


# 2. მომხმარებელს შეაყვანინე ასაკი, გადააქციე int-ად, მიუმატე 10 და დაბეჭდე შედეგი.
age = int(input("Enter your age: "))
print(age + 10)


# 3. მომხმარებელს შეაყვანინე ორი რიცხვი, ორივე გადააქციე int-ად და დაბეჭდე მათი ჯამი.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1 + num2)


# 4. მომხმარებელს შეაყვანინე სიმაღლე, გადააქციე float-ად და დაბეჭდე მისი ტიპი.
height = float(input("Enter your height: "))
print(type(height))


# 5. მომხმარებელს შეაყვანინე პროდუქტის ფასი, გადააქციე float-ად,
# მიუმატე 5.5 და დაბეჭდე შედეგი.
price = float(input("Enter product price: "))
print(price + 5.5)


# 6. შექმენი ცვლადები name, age და height.
# დაბეჭდე თითოეულის ტიპი type-ის გამოყენებით.
name = "Nika"
age = 15
height = 1.75

print(type(name))
print(type(age))
print(type(height))


# 7. მომხმარებელს შეაყვანინე სახელი და ასაკი.
# ასაკი გადააქციე int-ად და f-string-ის გამოყენებით დაბეჭდე:
# hello Nika you are 15 years old
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"hello {name} you are {age} years old")


# 8. მომხმარებელს შეაყვანინე ორი რიცხვი,
# ორივე გადააქციე int-ად და დაბეჭდე მათი ნამრავლი.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 * num2)


# 9. მომხმარებელს შეაყვანინე საყვარელი რიცხვი,
# გადააქციე int-ად, გამოაკელი 3 და დაბეჭდე შედეგი.
favorite_number = int(input("Enter your favorite number: "))

print(favorite_number - 3)


# 10. მომხმარებელს შეაყვანინე ასაკი, გადააქციე int-ად,
# შემდეგ დაბეჭდე:
# ასაკი
# ასაკს დამატებული 10
# ასაკის ტიპი type-ის გამოყენებით.
age = int(input("Enter your age: "))

print(age)
print(age + 10)
print(type(age))




