#The data we need to retrieve.
# 1.- The total number of votes cast
# 2.- A complete list of candidates who received votes
# 3.- The percentage of votes each candidate won
# 4.- The total number of votes each candidate won
# 5.- The winner of the election based on popular vote

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
<<<<<<< HEAD

# Open the election results and read the file.
#election_data = open(file_to_load, `r`) method 1
with open(file_to_load) as election_data:
    #To do: read and analyze the data here.
    #print(election_data)
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    #Print the header row.
    headers = next(file_reader)
    #print(headers)
    #Print each row in the CSV file.
=======
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
>>>>>>> 393f07404813dbe522943cb7f62ffb555efb7c6a
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
<<<<<<< HEAD
        #print(row)
        #2.1.- Print the candidate name from each row
        candidate_name = row[2]
        #2.2.- If the candidate does not match any existing candidate...
=======
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
>>>>>>> 393f07404813dbe522943cb7f62ffb555efb7c6a
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
<<<<<<< HEAD
            #2.3.- Begin tracking that candidate's vote count.
            candidate_votes[candidate_name]=0
        #2.4.- Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        
#2.5.- Save the results to our text file.
with open(file_to_save,"w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")
    print(election_results, end="")
    #Save the final vote count to the text file.
    txt_file.write(election_results)
      
    #3.- Print the total votes.
    #print(total_votes)
    #print(candidate_votes)
    #Determine the percentage of votes for each candidate by looping through the counts.
    #1.- Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #2.- retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #3.- Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes)*100
        #4.- Print the candidate name and percentage of votes
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        # To do: print out the winning candidate, vote count and percentage to terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        #Determine winning vote count and candidate
        #Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
            #And, set the winning_candidate equal to the candidate's name
            
    winning_candidate_summary = (
        f'---------------------------------\n'
        f'Winner: {winning_candidate}\n'
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------------\n")

    print(winning_candidate_summary)
    #Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
# Close the file.
#election_data.close() method 1

# Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w") method 1

#with open(file_to_save,"w") as txt_file:
    #Write some data to the file.
    #txt_file.write("Hello World")
    # Write three counties to the file.
    #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")


#outfile.write("Hello World") method 1

# Close the file
#outfile.close() method 1
=======
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
>>>>>>> 393f07404813dbe522943cb7f62ffb555efb7c6a
