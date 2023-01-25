# import dependencies 
import csv
import operator
import os

# Set relative path for csv file
Pybank_dataset = "./Resources/budget_data.csv"

total_months = 0
net_value = 0
current = 0
previous = 0 
PNL_chnages = 0 
list_changes = []
with open(Pybank_dataset, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:

        total_months = total_months +1
        net_value = int(row[1]) + net_value
        current = int(row[1]) 
        PNL_chnages = current - previous
        previous = int(row[1])
        list_changes.append(PNL_chnages)
        average_change = sum(list_changes)/len(list_changes)
        combined = list(zip(list_changes, range(len(list_changes))))
        greatest_increase = max(combined,key=operator.itemgetter(0))
        greatest_decrease = min(combined,key=operator.itemgetter(0))
print(total_months)
print(net_value)
print(list_changes)
print(average_change)
print(greatest_increase)
print(greatest_decrease)

#Printing the results of the analysis
printoutput = (
    f"Financial Analysis\n"
    f"-------------------------------------\n"
    f"Total Months: {str(total_months)}\n"
    f"Total: ${str(net_value)}\n"
    f"Average Change: ${str(round(average_change,2))}\n"
    f"Greatest Increase in Profits: {greatest_increase} (${str(greatest_increase)})\n"
    f"Greatest Decrease in Profits: {greatest_decrease} (${str(greatest_decrease)})\n")
print(printoutput)

# Exporttxtfile

output_file = "/Users/mollyfbg/PyBank/pybankanalysis/pyBankresult.txt"


pyBankresult = open(output_file, "w")

line1 = "Financial Analysis"
line2 = "------------------------------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(net_value)}")
line5 = str(f"Average Change: ${str(round(average_change,2))}")
line6 = str(
    f"Greatest Increase in Profits: {greatest_increase} (${str(greatest_increase)})")
line7 = str(
    f"Greatest Decrease in Profits: {greatest_decrease} (${str(greatest_decrease)})")
pyBankresult.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(
    line1, line2, line3, line4, line5, line6, line7))



