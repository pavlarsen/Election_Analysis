#The data we need to retrieve.
# 1.- The total number of votes cast
# 2.- A complete list of candidates who received votes
# 3.- The percentage of votes each candidate won
# 4.- The total number of votes each candidate won
# 5.- The winner of the election based on popular vote

import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file.
#election_data = open(file_to_load, `r`) method 1

with open(file_to_load) as election_data:

    #To do: read and analyze the data here.
    #print(election_data)
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Print the header row.
    headers = next(file_reader)
    print(headers)

    #Print each row in the CSV file.
    #for row in file_reader:
        #print(row)



# Close the file.
#election_data.close() method 1




# Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w") method 1

with open(file_to_save,"w") as txt_file:
    #Write some data to the file.
    #txt_file.write("Hello World")
    # Write three counties to the file.
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")


#outfile.write("Hello World") method 1

# Close the file
#outfile.close() method 1
