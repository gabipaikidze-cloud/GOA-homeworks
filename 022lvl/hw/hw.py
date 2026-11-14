
# დავალება 1
text = input("შეიყვანე ტექსტი: ")

text = text.strip().lower()

print(text)


# დავალება 2
password = input("შეიყვანე პაროლი: ")

print(password.isalnum())
print(password.isupper())


# დავალება 3
text = "Python Programming"

print(text.startswith("Py"))
print(text.find("Gram"))


# დავალება 4
text = input("შეიყვანე ტექსტი: ")

text = text.replace(" ", "-").upper()

print(text)


# დავალება 5
raw_data = "  html,css,javascript  "

raw_data = raw_data.strip()
words = raw_data.split(",")

print(words)


# დავალება 6
words = ["hello", "world", "python"]

words = [word.capitalize() for word in words]

result = "-".join(words)

print(result)


# დავალება 7
message = "  Hello World  "

message = message.lstrip()
message = message[::-1]

print(message)


# დავალება 8
text = input("შეიყვანე ტექსტი: ")

if text.isdigit():
    print(text[0:3])
else:
    print("ტექსტი შეიცავს არა მხოლოდ ციფრებს")


# დავალება 9
text = "Learning Python Is Fun"

text = text.lower()
words = text.split()

print(words)


# დავალება 10
word = "Database"

result = word[-3:].upper()

print(result)

