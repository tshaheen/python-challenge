import os
import csv

budget_data_csv = os.path.join("budget_data.csv")
total_months = 0
total_pl = 0
with open(budget_data_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)

    for row in csv_reader:
        #print(row[1])
        total_months = total_months + 1
        total_pl = total_pl + int(row[1])
print(total_months)
print(total_pl)
#row_count = sum(1 for row in budget_data_csv)
#print(row_count)
    