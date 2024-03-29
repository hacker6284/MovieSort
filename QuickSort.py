import random

def partition(movies, first, last):
    index = first
    pivot = last
    for i in range(first, last):
        answer = 0
        while answer != "1" and answer != "2":
            answer = input(f"(1) {movies[i]} or (2) {movies[pivot]}? ")
        if answer == "2":
            temp = movies[index]
            movies[index] = movies[i]
            movies[i] = temp
            index = index + 1
    temp = movies[pivot]
    movies[pivot] = movies[index]
    movies[index] = temp
    return index


def quick_sort(movies, first, last):

    if first < last:
        pi = partition(movies, first, last)
        quick_sort(movies, first, (pi - 1))
        quick_sort(movies, (pi + 1), last)


def sort(list):
    random.shuffle(list)
    quick_sort(list, 0, len(list) - 1)


def print_with_numbers(movies):
    for index, movie in enumerate(reversed(movies)):
        print(f"{index + 1}: {movie}")

if __name__ == "__main__":
    movie_list = open("movies.txt", "r").readlines()

    movies = []

    for movie in movie_list:
        movies.append(movie.strip())

    print(f"Length of movies list is {len(movies)}")

    random.shuffle(movies)

    for movie in movies:
        print(movie)

    print()

    quick_sort(movies, 0, len(movies) - 1)
    print_with_numbers(movies)
