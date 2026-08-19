
#```level 09:
#1) მომხმარებელს შემოატანინე ასაკი. თუ ასაკი არის 18 ან მეტი, დაბეჭდე:
#"შენ სრულწლოვანი ხარ."

#2) მომხმარებელს შემოატანინე რიცხვი. თუ ის დადებითია, დაბეჭდე:
#"დადებითი რიცხვია."

#3) მომხმარებელს შემოატანინე პაროლი. თუ პაროლი არის "python123", დაბეჭდე:
#"პაროლი სწორია."

#4) მომხმარებელს შემოატანინე თავისი ქულა. თუ ქულა არის 90 ან მეტი, დაბეჭდე:
#შესანიშნავი შედეგი!"

#5) მომხმარებელს შემოატანინე ტემპერატურა. თუ ტემპერატურა 0-ზე ნაკლებია, დაბეჭდე:
#"გარეთ ყინავს."

#6) მომხმარებელს შემოატანინე სახელი. თუ შემოტანილი სახელი არის "Giorgi", დაბეჭდე:
#"მოგესალმები, Giorgi!"

#7) მომხმარებელს შემოატანინე რიცხვი. თუ ის ლუწია, დაბეჭდე:
#"ლუწი რიცხვია."

#8) მომხმარებელს შემოატანინე თანხა. თუ თანხა არის 100 ან მეტი, დაბეჭდე:
#"შეგიძლია ფასდაკლების მიღება."

#9) მომხმარებელს შემოატანინე კვირის დღე. თუ შემოტანილია "Sunday", დაბეჭდე:
#"დღეს დასვენების დღეა."

#10) მომხმარებელს შემოატანინე ორი რიცხვი. თუ პირველი რიცხვი მეორეზე მეტია, დაბეჭდე:
#"პირველი რიცხვი უფრო დიდია."```

#1
age = int(input("Enter your age: "))

if age < 18:
    print("You are adult .")
#2
number = int(input("Enter a number: "))

if number > 0:
    print("Positive number.")
#3 
    password = input("Enter password: ")

if password == "python123":
    print("Correct password.")
#4
score = int(input("Enter your score: "))

if score >= 90:
    print("Excellent!")
#5
temperature = int(input("Enter the temperature: "))

if temperature < 0:
    print("It's freezing.")
#6
name = input("Enter your name: ")

if name == "Gabi":
    print("Hello, Gabi!")
#7    
number=int(input("enter a number: "))
if number % 2 == 0:
    print("Even number: ")
#8
   
salary = int(input("Enter your salary: "))

if salary > 100:
    print("Good salary.")
#9
day = input("Enter day: ")

if day == "Sunday":
    print("Day of rest.") 
#10
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number1 > number2:
    print("The first number is bigger.")        



