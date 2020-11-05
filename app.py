"""
User Story:
    - Add new movies to keep track of the movies
    - list all movies in the collection to be able to see them
    - find a movie by using movie title

    1. Decide where to store movies
    2. What data we need to store for each movie
    3. show the user menu for an options
    4. each requirement turn as a separate function
    5. Stop running the program when they type Q
"""

MENU_PROMPT = "\n Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title or 'q' to quit: "
movies = []


def add_movie():
    title = input("Enter movie title: ")
    director = input("Enter director name: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def print_movie(movie):
    print(f"{movie['title'].title()} by {movie['director'].title()}, produced in {movie['year']}")


def list_movies():
    for movie in movies:
        print_movie(movie)


def find_movie():
    user_input = input("Enter the movie title: ")

    for movie in movies:
        if user_input.lower() == movie['title'].lower():
            print("We found the movie:")
            print_movie(movie)
        else:
            print(f"{user_input} has not been found in the list of movies.")


user_options = {
    "a": add_movie,
    'l': list_movies,
    'f': find_movie
}


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            user_options[selection]()
            # selected_function = user_options[selection]
            # selected_function()
        else:
            print("Unknown command, please try again.")

        selection = input(MENU_PROMPT)


menu()
