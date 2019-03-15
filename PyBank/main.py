import os
import csv
#  Your task is to create a Python script that analyzes the records to calculate each of the following:

#   * The total number of months included in the dataset

#   * The total net amount of "Profit/Losses" over the entire period

budget_data_csv = os.path.join("budget_data.csv")
total_number_months = 0
total_pl = 0
pl_list=[]
month_change = []
increase = ["", 0]
decrease = ["", 500000000]

with open(budget_data_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)

    first_row = next(csv_reader)
    total_number_months = total_number_months + 1
    total_pl = total_pl + int(first_row[1])
    monthly_pl = int(first_row[1])   
    
    for row in csv_reader:
        
        total_number_months = total_number_months + 1
        total_pl = total_pl + int(row[1])
    
        change_in_pl = int(row[1]) - monthly_pl
        monthly_pl = int(row[1])
        pl_list = pl_list + [change_in_pl]
        month_change = month_change + [row[0]]  

        if change_in_pl > increase[1]:
            increase[0] = row[0]
            increase[1] = change_in_pl

        if change_in_pl < decrease[1]:
            decrease[0] = row[0]
            decrease[1] = change_in_pl

# print(increase)
# print(total_number_months)
# print(total_pl)


# #   * The average change in "Profit/Losses" between months over the entire period

Average_Monthly_Change = sum(pl_list) / len(pl_list)
# print(Average_Monthly_Change)


# #   * The greatest increase in profits (date and amount) over the entire period



    # change_in_pl = int(row[1]) - monthly_pl
    # monthly_pl = int(row[1])
    # pl_list = pl_list + [change_in_pl]
    # month_change = month_change + [row[0]]


        

# #   * The greatest decrease in losses (date and amount) over the entire period


        
# print(decrease)

# * In addition, your final script should both print the
# to the terminal and export a text file with the 
# results.

output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_number_months}\n"
    f"Total: ${total_pl}\n"
    f"Average  Change: {Average_Monthly_Change:.2f}\n"
    f"Greatest Increase in Profits: {increase[0]} ({increase[1]})\n"
    f"Greatest Decrease in Profits: {decrease[0]} ({decrease[1]})\n")

print(output)
export_file = os.path.join("export_file.txt")

with open(export_file, "w") as txt_file:
    txt_file.write(output)

# # * As an example, your analysis should look similar to the one below:

# #   ```text
# #   Financial Analysis
# #   ----------------------------
# #   Total Months: 86
# #   Total: $38382578
# #   Average  Change: $-2315.12
# #   Greatest Increase in Profits: Feb-2012 ($1926159)
# #   Greatest Decrease in Profits: Sep-2013 ($-2196167)
# #   ```

    