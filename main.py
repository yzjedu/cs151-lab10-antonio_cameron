# Programmers:  Antonio, Cameron
# Course:  CS151, Professor Z
# Due Date: november 21
# Lab Assignment:  Lab 10
# Problem Statement:  In this lab assignment you will analyze data on movies, their budgets, and their profits
# Data In:
# Data Out:
# Credits:
# Input Files: Movies.csv

def read_file(filename):
    table = []

    try:
        file = open(filename, "r")
        for line in file:
            row = line.split()

        file.close()

    except FileNotFoundError:
        print("File doesn’t exist")

def compute_profit(movies):

    for movie in movies:
        budget = movie[2]
        worldwide_gross = movie[4]
        profit = worldwide_gross - budget
        movie.append(profit)  # Add profit as the last element
    return movies

def main():



