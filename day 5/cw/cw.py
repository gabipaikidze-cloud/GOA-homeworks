# Level 05


# 1. შექმენი ცვლადი name, შეინახე შენი სახელი და დაბეჭდე მისი მნიშვნელობა და ტიპი.
name = "Giorgi"
print(name)
print(type(name))


# 2. შექმენი ცვლადი age, შეინახე შენი ასაკი და დაბეჭდე მისი მნიშვნელობა და ტიპი.
age = 18
print(age)
print(type(age))


# 3. მომხმარებელს შეაყვანინე ასაკი input()-ით, გადააქციე int-ად და დაბეჭდე მისი ტიპი.
age = int(input("Enter your age: "))
print(type(age))


# 4. მომხმარებელს შეაყვანინე სიმაღლე input-ით, გადააქციე float-ად და დაბეჭდე მისი ტიპი.
height = float(input("Enter your height: "))
print(type(height))


# 5. მომხმარებელს შეაყვანინე სახელი, ასაკი და სიმაღლე.
# შემდეგ დაბეჭდე ეს ინფორმაცია f-string-ის გამოყენებით.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print(f"My name is {name}, I am {age} years old and my height is {height}.")

