# Algorithm Document

### Purpose: read the information in the movies.csv and convert it to a list
### Name: read_file
### Parameters: filename
### Return: movies
### Algorithm:
1. try to open file as indicated by user to read
2. for every line in file:
   1. strip and split every line in the file
   2append data to list 'movies'
3. close file
4. return movies

### Purpose: compute the total profit of a movie and append it to the list 
### Name: compute_profit
### Parameters: movies
### Return: updated_movies
### Algorithm: 
1. create a list named updated_movies
2. for every movie in movies:
   1. create budget variable and equal it to movie[2]
   2. create worldwide gross variable and equal it to movie[4]
   3. create profit variable and equal it to worldwide gross minus budget
   4. append movie and corresponding provit variable to the updated_movies list
3. return updated_movies


### Purpose: main function
### Name: main
### Parameters: none
### Return: none
### Algorithm:
1. ask user to enter name of file
2. call read_file
3. call compute profit
4. open file titled updated_movie_list.csv to write
5. for every movie in updated_movies list:
   1. write all lines in updated_movies to updated_movie_list.csv
6. close file
7. for every movie in updated movies:
   1. print movie