# 1) შექმენი Dictionary სახელად student, რომელშიც შეინახავ მოსწავლის სახელს, ასაკს და კლასს. შემდეგ დაამატე ახალი Key city, რომელშიც შეინახავ ქალაქის სახელს. დაბეჭდე განახლებული Dictionary.
student = {
    "name": "Gabriel",
    "age": 15,
    "class": 9
}

student["city"] = "Tbilisi"

print(student)
# 2) შექმენი Dictionary სახელად car, რომელშიც შეინახავ მანქანის ბრენდს, მოდელს, გამოშვების წელს და ფერს. შემდეგ წაშალე Dictionary-დამ color Key და დაბეჭდე განახლებული Dictionary.
car = {
    "brand": "BMW",
    "model": "M5",
    "year": 2022,
    "color": "Black"
}

del car["color"]

print(car)
# 3) შექმენი Dictionary სახელად book, რომელშიც შეინახავ წიგნის სათაურს, ავტორს და გვერდების რაოდენობას. მომხმარებელს შემოატანინე ინფორმაცია და შეამოწმე in ოპერატორის გამოყენებით, არსებობს თუ არა მის მიერ შეყვანილი Key ობიექტში. დაბეჭდე შესაბამისი შეტყობინება.
book = {
    "title": "Harry Potter",
    "author": "J.K. Rowling",
    "pages": 350
}

key = input("Enter a key: ")

if key in book:
    print("Key exists!")
else:
    print("Key does not exist!")
# 4) შექმენი Dictionary სახელად phone, რომელშიც შეინახავ ტელეფონის ბრენდს, მოდელს და ფასს. შემდეგ შეცვალე ტელეფონის ფასი და მოდელი ახალი მნიშვნელობებით. დაბეჭდე განახლებული Dictionary.
phone = {
    "brand": "Samsung",
    "model": "Galaxy S23",
    "price": 2000
}

phone["price"] = 2500
phone["model"] = "Galaxy S24"

print(phone)
# 5) შექმენი Dictionary სახელად game, რომელშიც შეინახავ თამაშის სახელს, ჟანრს და რეიტინგს. შემდეგ:
# დაამატე ახალი Key developer, რომელშიც შეინახავ თამაშის შემქმნელის სახელს.
# შეამოწმე in ოპერატორით, არსებობს თუ არა rating Key.
# წაშალე genre Key.
# შეცვალე თამაშის სახელი.
# დაბეჭდე საბოლოო ობიექტი.
game = {
    "name": "Minecraft",
    "genre": "Sandbox",
    "rating": 9
}

game["developer"] = "Mojang"

if "rating" in game:
    print("Rating key exists!")
else:
    print("Rating key does not exist!")

del game["genre"]

game["name"] = "Roblox"

print(game)