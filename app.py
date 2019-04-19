"""
Enter
'a' to add a movie,
'l' to see your movies,
'f' to find a movie, and
'q' to quit:


Tasks:
[x]: Decide where to store movies
[]: What is the format of a movie?
[x]: Show the user the main interface and get their input
[x]: Allow users to add movies
[]: Show all their movies
[]: Find a movie
[x]: Stop running the program when they type 'q'
"""

movies = []

"""
movie - {
    'name' 
"""


def menu():
    user_input = input("Enter \n"
                       "'a' to add a movie\n"
                       "'l' to see your movies\n"
                       "'f' to find a movie\n"
                       "'q' to quit:\n")
    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            find_movie()
        else:
            print('Unknown command, please try again.')

        user_input = input("\nEnter \n"
                           "'a' to add a movie\n"
                           "'l' to see your movies\n"
                           "'f' to find a movie, and\n"
                           "'q' to quit:\n")


def add_movie():
    name = input('Enter the movie name: ')
    director = input('Enter the movie director: ')
    year = int(input('Enter the movie release year: '))

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def show_movies():
    for movie in movies:
        print(f"Name: {movie['name']}")
        print(f"Director: {movie['director']}")
        print(f"Release year: {movie['year']}")
        print(" ")


menu()
