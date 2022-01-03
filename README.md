# Analysis of Election Audit

## Project Overview
An audit of a local congressional election was requested by the Colorado Board of Elections. 

The following tasks were requested for the audit:

1. Determine the total number of votes cast in the local election.
2. Create a list of the candidates who received votes.
3. Calculate the total votes and percentage of votes for each candidate.
4. Calculate the voter turnout and percentage of votes for each county audited.
5. Determine the county with the highest voter turnout.
5. Determine the winner of the election based on the highest percentage of the popular vote.

## Project Resources

The source data provided by the elections office is election_results.csv.

This audit was perfomed using Python 3.7 and Visual Studio Code v1.63.2. 

## Election-Audit Results (bulleted list for results with examples of code)
For each of the audit results, the code used to obtain the results from the data set follow the election results. 
- The results of the audit of this local congressional elections showed a total of **369,711** votes cast. 
- - The code used to obtain the total votes was obtained by first zeroing the total_votes. Once the file was opened and read, the count for total_votes was incremented for each row in the source file. The header row was ignored to ensure an accurate count of total votes.
(link to screen shot of code used)

- There were three counties contained in the data set. The total votes and percentage of votes by county were:
- - Jefferson County had 10.5% of the total votes with 38,355 votes cast.
- - Denver County had 82.8% of the total votes with 306,055 votes cast.
- - Arapahoe County had 6.7% of the votes with 24,801 votes cast.
- In this congressional election, Denver County had the highest voter turnout.
- - The code to determine voter turnout is shown below.
(link to screenshot of voter turnout code used)

- The candidates, vote percentage and vote totals were:

- - Charles Casper Stockham received 23.0% of the total votes with 85,213 votes.
- - Diana DeGette received 73.8% of the total votes with 272,892 votes.
- - Raymon Anthony Doane received 3.1% of the total votes with 11,606 votes.
(link to code used)

The audit showed the winner of the local congressional election to be **Diana DeGette** with **73.8%** of the total votes by winning a total of **272,892** votes.
(link to code used)

All results can be seen here in a screenshot of the program used to analyze the data:
(link to screenshot).

# Election-Audit Summary and Recommendations
Python is an open-source computer programming language that is easy to understand as it uses the same syntax as English. The programming code used for this audit employed powerful dependencies, modules and packages within the Python program which allowed faster programming by use of pre-written code. In this audit, use of the `csv module` allows reading and writing tabular data while the `os module` allows interaction with the computer operating system to find the correct place to access and save data files. 

![Import csv](https://github.com/Bscheinin/Election_Analysis/blob/main/Resources/Module%20code.PNG)

By chaining these modules with the `(join)` function, access to the data file and the path in which to save the data was quickly determined. 

Use of the powerful resources within Python such as dependencies, modules and packages, could allow access to and analysis of larger data sets such as representative races to state-wide presidential contests. (code modification examples)

