import csv
from pathlib import Path
import os

bank_data_filtered = [["Bank of Big - Premier Option",300000,0.85,0.47,740,3.6],
                      ["Bank of America - Plusn",500000,0.85,0.47,750,3.5],]
out_dir = './rep'
file_name = "list_of_qualified_loans.csv"
full_path = os.path.join(out_dir,file_name)
# module stars here, all above are in main app file

qualy_loans_header = ["Lender","Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Int Rate"]

Path(file_name) #this is the file name to be written to/created 
with open(full_path, 'w', newline='') as csvfile: #the 'w' indicates we are writing to the file, newlins is to manage especial characters
    csvwriter = csv.writer(csvfile) #csvwriter is the writing function from the csv library imported at the begining
# Write our header row first
    csvwriter.writerow(qualy_loans_header)
# Then we can write the data rows
    # for row in bank_data_filtered :
    csvwriter.writerows(bank_data_filtered)

print(f"The file 'list_of_qualified_loans.csv' was saved in:{out_dir}")