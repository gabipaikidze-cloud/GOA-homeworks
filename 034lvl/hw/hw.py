# დავალება 1
even_numbers = {2, 4, 6, 8, 10}
odd_numbers = {1, 3, 5, 7, 9}

all_numbers = even_numbers.union(odd_numbers)

print(all_numbers)
print("ელემენტების რაოდენობა:", len(all_numbers))


# დავალება 2
favorite_movies = {
    "Avatar",
    "Titanic",
    "Harry Potter",
    "Spider-Man",
    "The Lion King"
}

popular_movies = {
    "Avatar",
    "Titanic",
    "Fast and Furious",
    "The Avengers",
    "Spider-Man",
    "Joker"
}

common_movies = favorite_movies.intersection(popular_movies)

print("საერთო ფილმები:", common_movies)


# დავალება 3
group_a = {5, 10, 15, 20, 25}
group_b = {15, 20, 25, 30, 35}

all_numbers = group_a.union(group_b)
common_numbers = group_a.intersection(group_b)

print("ყველა უნიკალური რიცხვი:", all_numbers)
print("საერთო რიცხვები:", common_numbers)
print("საერთო ელემენტების რაოდენობა:", len(common_numbers))


# დავალება 4
monday = {"Giorgi", "Nika", "Luka", "Ana", "Saba", "Mariam"}
tuesday = {"Giorgi", "Nika", "Ana", "Saba", "Dato", "Luka"}
wednesday = {"Giorgi", "Nika", "Ana", "Mariam", "Saba", "Luka"}

all_days_students = monday.intersection(tuesday)
all_days_students = all_days_students.intersection(wednesday)

print("სამივე დღეს დამსწრე მოსწავლეები:", all_days_students)
print("მოსწავლეების რაოდენობა:", len(all_days_students))


# დავალება 5
available_books = {
    "Harry Potter",
    "The Hobbit",
    "The Little Prince",
    "Alice in Wonderland",
    "Robinson Crusoe",
    "The Alchemist"
}

new_books = {
    "Harry Potter",
    "The Alchemist",
    "The Great Gatsby",
    "Sherlock Holmes"
}

existing_books = available_books.intersection(new_books)

updated_books = available_books.union(new_books)

print("წიგნები, რომლებიც უკვე არსებობს:", existing_books)
print("განახლებული ბიბლიოთეკა:", updated_books)
print("საბოლოო წიგნების რაოდენობა:", len(updated_books))