# **UCB FinTech Bootcamp Module 2 Challenge**
# *Loan Qualifier*
## Introduction

    The Bootcamp Module 2 Challenge - Loan Qualifier consists of a modular solution to solve for a loan application and loan evaluation scenario. 
    The loan officer (the user) uses the solution to capture customer provided financial data, calculate additional financial parameters for loan evaluation (e.g.ratios) and then, out of a predetermined list of lenders and their criteria, find the ones that match customer's financial parameters. This qualification process results in a list of qualified loans, which the loans officer has the option to save to a csv file and to a location of their choice.
---
## Goals and Objectives

    The objective is to provide a programatic solution (the application) that allows the automation of the loan qualification process by:

    1. Providing dynamic data entry capabilities (e.g not from a static list or as predetermined values), 
    2. Automate calculation of relevant ratios (Income ratio and Loan-to-Value) to complete the customer financial data set
    3. Automated filtering of qualified loans, comparing the customer fiancial data set versus the list of lender criteria (e.g. the daily rate sheet) and prepare a list of these qualified loan options
    4. And finally, provide the loans officer with the option to save the list of qualified options to a fiel and folder of his choice

#### These four main areas described above are described in detailed in the [User Stories](https://github.com/LUTOV001/2.Loan-Qualifyer/blob/main/2.Loan_Qualifyer_user_stories.txt), along with their Pass criteria
---
## Technologies and Tools
    The following list includes the main technologies and tools using during the preparation and deployment of the solution:

    1. *Python* - Programming language used to code the solution. Version 3.7.13 was used
    2. *GitHub* - Reposotory for code deployment, version management and documentation of the presented solution
    3. *MS Virtual Studio Code* - IDE tool for coding, code testing/debugging and solution documentation. Version V1.77.0 was used
    4. *Git Bash console* - Local console used to test the coded solution. Version 2.40.0.windows.1 was utilized
    5. *Slack* - Collaboration tool to communicate and brainstorm with other FinTech Bootcamp participants
    6. *Operative System* - This solution was prepared in a PC running Windows 11 v H22
---
## Installation Guide

    The following Python modules need to be installed for the provided solution to work as designed and built
#### a.[Quesionary](https://lyz-code.github.io/blue-book/questionary/) 
#### b.[Fire](https://github.com/google/python-fire)


---
## Solution Structure

The [Loan Qualifier](https://github.com/LUTOV001/2.Loan-Qualifyer) repository in GitHub contains all solution components.

The repository consists of the following folders, subfolders and contents as described below:
 
    1. data : Includes the list of available loans, by lenders and their criteria:  daily_rate_sheet.csv
    2. images : contains the screenshots used in the detailed user instructions below
    3. new_04_2_23 : folder created while testing the option to save the csv file to a non pre-existing folder, this is the new folder created with that option
    4. output : pre created folder to save list of qualified loans (csv file) if the user does not want to create a new folder, like the one above
    5. qualifier: directory containing modules of the solution in the sub-folders below
    | 5.1 filters: Contains the python modules used to filter the loans for each finance parameter as follows
        credit_score.py : filters by credit score number provided by customer vs lender criteria
        debt_to_income.py: filters by debt to income (calculated) ratio vs lender criteria
        loan_to_value.py : filters by loan to value ratio (calculated) vs. lender criteria
        max_loan_size.py: filters by loan amount vs lender criteria
    | 5.2 utils : contains utility programs used for automated/modular functions like calculations, inputs (read csv) and outputs (write csv)
        calculators.py : includes the logic for ratio calculations, debt to income and loan to value
        fileio.py : This contains a helper function for loading and saving CSV files
        cti_file_save.py : includes stand alone logic for the cti interaction to decide whether or not to save the list of loans and where
        file_save.py : includes stand alone logic to save the cvs file to the location provided by the user
    6. 2.Loan_Qualifier_user_stories.txt : User stories and pass criteria for translate requirements onto the code in the solution
    7. README.md - The file containing this present document
    8. app.py : This is the main Phyton program containing the code the user will run to operate the solution <==
    9. terminal_history.txt : text file with the log of the 50 most recent commands executed in the terminal

## User Instructions
From the Git Bash terminal (Windows), navigate to the directory where the Github repository is cloned
![path](https://github.com/LUTOV001/2.Loan-Qualifyer/blob/main/images/terminal_github_repo.jpg)
```


### Credits

Prepared by Luis Torres 
LUTOV001@gmail.com
April 2023

---

