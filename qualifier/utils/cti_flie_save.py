import questionary
from pathlib import Path
import csv
import os


"""Ask if the user wants to save the list of qualified loans to a file
If so, ask for the file path to save the list to (e.g. ./output) of qualified loans and the <file_name>.csv (e.g. list_of_qualified_loans.csv)

    Returns:
        If the user wants to save the data from the filtered list, it is saved with the <file_name>.csv in the path requested (folder or directory)
        If the user does not want to save the file, a message with the decision not to save the list is displayed
    """
bank_data_filtered = [["Bank of Big - Premier Option",300000,0.85,0.47,740,3.6],
                      ["Bank of America - Plus",500000,0.85,0.47,750,3.5],
                      ["Wells Fargo - N'sider",400000,0.85,0.40,760,3.2],]

def save_qualifying_loans(qualifying_loans):
    # qualifying_loans = bank_data_filtered
    save_file = questionary.text("Do you want to save the list of qualified loans?(Yes/No)").ask()

    if save_file =="Yes" :
            out_dir = questionary.text("Enter the directory/folder where you want to save the file:").ask()
            file_name = questionary.text("Enter a file name with extension .csv (e.g. qualified_loans.csv):").ask()
            # csvpath = Path(out_dir)
            if not os.path.exists(out_dir):
                    os.makedirs(out_dir)
                    print(f'The directory/folder {out_dir} was created')
    else :
            print("The list of qualified loans WILL NOT be saved")
        
    full_path = os.path.join(out_dir,file_name)
        
    qualy_loans_header = ["Lender","Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Int Rate"]

    Path(file_name) #this is the file name to be written to/created per the users input in the CTI
    with open(full_path, 'w', newline='') as csvfile: #the 'w' indicates we are writing to the file, newlins is to manage especial characters
        csvwriter = csv.writer(csvfile) #csvwriter is the writing function from the csv library imported at the begining
    # Write our header row first
        csvwriter.writerow(qualy_loans_header)
    # Then we can write the list to the file
        # for row in bank_data_filtered :
        csvwriter.writerows(bank_data_filtered)

    print(f"The file {file_name} was saved in the directory/folder:{out_dir}")

