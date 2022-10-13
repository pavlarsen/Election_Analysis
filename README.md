# Election Analysis

## Overview of Project

### A Colorado Board of Elections needed help on determining total number of votes, list of candidates and their respective results, determine the election winner, share of votes received as well as an analysis of trends among counties that participated in the electoral process. Luckily, with a little bit of Python magic, all these answers can be solved in a short amount of time.

---

## Election - Audit Results

It's election night in Colorado and everyone is wondering who the next congressional leader will be. The Colorado Board will have to cast all votes within the counties of Denver, Jefferson and Arapahoe. According to media outlets, around 350K people went to the polls this morning. For the Board to be able to count each vote and determine the election winner in other period would have represented days of counting and high costs of people, luckily with Python, it is possible to provide general information about the election such as total votes, candidates vote (amounts and percentage), counties votes (amounts and percentage), election winner.

For this project, it was a huge help to be able to implement Python coding for quickly computing information from the polls.

The overall election results were saved in a CSV file. With the following Python code, it was possible to read the file in a Python environment as well as create and save a new text file to save our results:

![Captura de Pantalla 2022-10-12 a la(s) 19 51 03](https://user-images.githubusercontent.com/113866707/195473967-7269869c-baf8-4c6f-abeb-22fc3d4d413c.png)


Before jumping into results, Python required to have certain variables expressed. This process will help us run the calculations later during the code: 

![Captura de Pantalla 2022-10-12 a la(s) 19 52 38](https://user-images.githubusercontent.com/113866707/195474116-b963aff7-4537-459a-86a7-efaaeaa9b4fd.png)

As you can see, we are setting our votes counting starting at 0, created a list of candidates, and a dictionary to pull the votes each candidate received. The same process was followed for county level analysis. Finally, we just needed to set the variables for winning candidate, number of votes and percentage as well a county with most votes and number of votes.

The next steps, required our Python code to start reading the data in the CSV and start performing actions, following certain condition and run calculations for total votes per candidate and county:

![Captura de Pantalla 2022-10-12 a la(s) 19 57 37](https://user-images.githubusercontent.com/113866707/195474669-8b58f1d8-f403-47df-b9cd-750bd20e5daa.png)
![Captura de Pantalla 2022-10-12 a la(s) 19 58 19](https://user-images.githubusercontent.com/113866707/195474755-d0a7a706-d5be-4271-90ae-01c3f29c34b5.png)

Since we need to be able to visualize the results either in the Terminal or in the text file we created previously, we then tell Python how we want the output to look like with the following piece of the code:

![Captura de Pantalla 2022-10-12 a la(s) 20 01 17](https://user-images.githubusercontent.com/113866707/195475037-fb0e7455-5b79-4b33-ad8f-a6d86afbf8fc.png)

For the respective county analysis, we just loop thru the CSV data and start computing the votes for each county. Then we save the output into our text file:

![Captura de Pantalla 2022-10-12 a la(s) 20 03 15](https://user-images.githubusercontent.com/113866707/195475301-d19d7055-5752-48d6-aba3-418e963df621.png)

We enter the next code for performing the analysis on candidate level. This is the part that will tell us which is the winner!

![Captura de Pantalla 2022-10-12 a la(s) 20 05 19](https://user-images.githubusercontent.com/113866707/195475488-0e825d6d-6154-430c-a7ed-1340cd1a9d34.png)

Finally, we can answer some questions: 

![Captura de Pantalla 2022-10-12 a la(s) 20 07 24](https://user-images.githubusercontent.com/113866707/195475626-bd307538-9ca7-4e99-8a1c-da220d86f149.png)

Congratulations to Diana DeGette! New congressional leader with astonishing 73.8% of the votes (272,892) from a total of 369,711 votes. 
On second place we have Charles Casper with 23% of the votes (85,213) and in third place is Raymon Doane which was only able to convince 3.1% of the voters.
Denver was the county with most votes in this election, accounting for 82.8% of the total votes.
    
---

## Summary

- As we can see, we can leverage the power of Python to perform not just this election analysis, but even 2024 Presidential Election. With Python, we will be able to enter via conditionals the different requirements per electoral district to determine the winner of the district and then keep adding towards a total amount. We can set the assigned level of electoral votes to the winner and finally be able to determine who the winner is.

- For this code, it would be interesting to identify how many votes did any candidate got from each county. This would help the election teams to perform a better campaign for the next election. It would also be interesting to add other variables to the original dataset regarding age, gender and other data that could help us understand who the average voter is.

