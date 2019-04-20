"""
Enter
'a' to add a movie,
'l' to see your movies,
'f' to find a movie, and
'q' to quit:


Tasks:
[x]: Decide where to store movies
[x]: What is the format of a movie?
[x]: Show the user the main interface and get their input
[x]: Allow users to add movies
[x]: Show all their movies
[x]: Find a movie
[x]: Stop running the program when they type 'q'
"""

movies = []

"""
movie - {
    'name': ... (str),
    'director': ... (str),
    'year': ... (int)
    }
"""


def menu():
    user_input = input("\nEnter \n"
                       "'a' to add a movie\n"
                       "'l' to see your movies\n"
                       "'f' to find a movie\n"
                       "'q' to quit:\n")
    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
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
    year = (input('Enter the movie release year: '))

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def show_movies(movies_list):
    for movie in movies_list:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"\nName: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")


def find_movie():
    find_by = input("What property of the movie are you looking for? ")
    looking_for = input("What are you searching for? ")

    found_movies = find_by_attribute(looking_for, lambda x: x[find_by])

    show_movies(found_movies)


def find_by_attribute(expected, finder):
    found = []

    for movie in movies:
        if finder(movie) == expected:
            found.append(movie)

    return found


menu()

"""
 movies = find_by_attribute(looking_for, lambda x: x[find_by])


def find_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)

    return found

"""
