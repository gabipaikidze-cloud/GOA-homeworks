# ```level 38:
# 1) შექმენი Dictionary სახელად laptop, რომელშიც შეინახავ ლეპტოპის ბრენდს, მოდელს, RAM-ის მოცულობას და ფასს. შემდეგ დაამატე ახალი Key storage, რომელშიც შეინახავ მეხსიერების მოცულობას. დაბეჭდე განახლებული Dictionary.
laptop = {
    "brand": "HP",
    "model": "Pavilion",
    "RAM": "16GB",
    "price": 2500
}

laptop["storage"] = "512GB SSD"

print(laptop)
# 2) შექმენი Dictionary სახელად teacher, რომელშიც შეინახავ მასწავლებლის სახელს, გვარს, ასაკს და საგანს. შემდეგ წაშალე age Key და დაბეჭდე განახლებული Dictionary.
teacher = {
    "name": "Giorgi",
    "surname": "Beridze",
    "age": 35,
    "subject": "Math"
}

del teacher["age"]

print(teacher)
# 3) შექმენი Dictionary სახელად country, რომელშიც შეინახავ ქვეყნის სახელს, დედაქალაქს, მოსახლეობას და ფართობს. მომხმარებელს შემოატანინე Key და in ოპერატორის გამოყენებით შეამოწმე, არსებობს თუ არა ეს Key Dictionary-ში. დაბეჭდე შესაბამისი შეტყობინება.
country = {
    "name": "Georgia",
    "capital": "Tbilisi",
    "population": 3700000,
    "area": 69700
}

key = input("Enter a key: ")

if key in country:
    print("Key exists")
else:
    print("Key does not exist")
# 4) შექმენი Dictionary სახელად product, რომელშიც შეინახავ პროდუქტის სახელს, კატეგორიას, ფასს და რაოდენობას. შემდეგ შეცვალე პროდუქტის ფასი და რაოდენობა ახალი მნიშვნელობებით. დაბეჭდე განახლებული Dictionary.
product = {
    "name": "Laptop",
    "category": "Electronics",
    "price": 2000,
    "quantity": 10
}

product["price"] = 1800
product["quantity"] = 15

print(product)
# 5) შექმენი Dictionary სახელად school, რომელშიც შეინახავ სკოლის სახელს, მოსწავლეების რაოდენობას და ქალაქს. შემდეგ:
# - დაამატე ახალი Key director, რომელშიც შეინახავ დირექტორის სახელს.
# - შეამოწმე in ოპერატორით, არსებობს თუ არა students Key.
# - წაშალე city Key.
# - შეცვალე სკოლის სახელი.
# - დაბეჭდე საბოლოო Dictionary.
school = {
    "name": "Green School",
    "students": 500,
    "city": "Tbilisi"
}

school["director"] = "Nino"

if "students" in school:
    print("Students key exists")
else:
    print("Students key does not exist")

del school["city"]

school["name"] = "Blue School"

print(school)
# 6) შექმენი Dictionary სახელად footballer, რომელშიც შეინახავ ფეხბურთელის სახელს, ასაკს, გუნდს და გატანილი გოლების რაოდენობას. შემდეგ დაამატე ახალი Key position, რომელშიც შეინახავ ფეხბურთელის პოზიციას. შეცვალე მისი ასაკი და გოლების რაოდენობა. დაბეჭდე განახლებული Dictionary.
footballer = {
    "name": "Cristiano Ronaldo",
    "age": 40,
    "team": "Al Nassr",
    "goals": 900
}

footballer["position"] = "Forward"

footballer["age"] = 41
footballer["goals"] = 950

print(footballer)
# 7) შექმენი Dictionary სახელად movie, რომელშიც შეინახავ ფილმის სახელს, რეჟისორს, გამოშვების წელს და ჟანრს. მომხმარებელს შემოატანინე Key და შეამოწმე in ოპერატორით, არსებობს თუ არა ის Dictionary-ში. შემდეგ წაშალე year Key და დაბეჭდე საბოლოო Dictionary.```
movie = {
    "name": "Titanic",
    "director": "James Cameron",
    "year": 1997,
    "genre": "Romance"
}

key = input("Enter a key: ")

if key in movie:
    print("Key exists")
else:
    print("Key does not exist")

del movie["year"]

print(movie)