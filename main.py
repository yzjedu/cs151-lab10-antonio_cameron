# Programmers:  Antonio, Cameron
# Course:  CS151, Professor Z
# Due Date: november 21
# Lab Assignment:  Lab 10
# Problem Statement:  In this lab assignment you will analyze data on movies, their budgets, and their profits
# Data In: user inputs name of file
# Data Out: list of movie release date, movie title, movie budget, domestic gross, worldwide gross, movie profit
# Credits: class discussion
# Input Files: Movies.csv

# Name: read_file
# Parameters: filename
# Return: movies
def read_file(filename):
    movies = []
    try:
        file = open(filename, "r")
        for line in file:
            row = line.strip().split(",")
            movies.append(row)
        file.close()
    except FileNotFoundError:
        print("File doesn’t exist")
    return movies

# Name: compute_profit
# Parameters: movies
# Return: updated_movies
def compute_profit(movies):
    updated_movies = []
    for movie in movies:
        try:
            budget = float(movie[2])
            worldwide_gross = float(movie[4])
            profit = worldwide_gross - budget
            updated_movies.append(movie + [profit])
        except (IndexError, ValueError):
            print(f'Error processing movie')
    return updated_movies

# Name: main
# Parameters: None
# Return: None
def main():
    print('Hello! In this program you can enter the name of a file with different information about several movies,\n'
          'and receive different outputs containing summarized information about the movies.')
    filename = input("Enter a file name: ")
    movies = read_file(filename)
    if movies:
        updated_movies = compute_profit(movies)
        file = open('updated_movie_list.csv', 'w')
        for movie in updated_movies:
            for i in range(len(movie)):
                file.write(str(movie[i]))
                if i < len(movie) - 1:
                    file.write(",")
            file.write("\n")
        file.close()
        print("Updated Movies Data:")
        for movie in updated_movies:
            print(movie)

main()


