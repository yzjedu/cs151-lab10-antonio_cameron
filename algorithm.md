# Algorithm Document

1 function for correct file name
1 function for reading file name from user

2 function to read data from file into a list of lists
2 function to output file with movie information and new column for movie profit

3 function for writing data plus profit to a new file,
3 function for finding highest/lowest revenue movie

4 main function calls all other functions



# Purpose: create list of lists
# Name: file_to_list
# Parameters: file
# Return: lists
# Algorithm:
1. set table equal to []
   1. try
      1. open the file
      2. for each line in file
         1. split line at ','
   2. except
      1. output file not found/ does not exist
   3. return the table

# Purpose: append profit to lists
# Name: add_profit
# Parameters: 
# Return: appended lists
# Algorithm:
1. Add a new variable, profit = worldwide_gross - budget. 
2. If worldwide_gross is 0, set profitability to -budget to indicate a loss.






# Purpose: highest/lowest revenue
# Name: movie_revenue
# Parameters: 
# Return: revenue
# Algorithm:
1. Total number of movies. 
2. Average, minimum, and maximum for:
   3. Budget. 
   4. Domestic gross. 
   5. Worldwide gross. 
   6. Total profitability. 
7. Identify top 5 movies for:
   8. Worldwide gross. 
   9. Profitability. 
   10. Budget. 
   11. Analyze trends by year:
   12. Group movies by release year. 
   13. Calculate yearly averages for budget and worldwide gross.

1. Return a dictionary containing:
   2. Cleaned movies data.
   3. statistics with calculated insights.

# Purpose: call other functions
# Name: main
# Parameters: none 
# Return: none
# Algorithm:
1. call other functions