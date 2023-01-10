import csv

pybank_dataset = "PyBank/Resources/budget_data.csv"

total_months = 0
net_value = 0
current = 0
previous = 0 
PNL_chnages = 0 
list_changes = []
with open(pybank_dataset, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:

        total_months = total_months +1
        net_value = int(row[1]) + net_value
        current = int(row[1]) 
        PNL_chnages = current - previous
        previous = int(row[1])
        list_changes.append(PNL_chnages)
        
print(total_months)

print(net_value)

print(list_changes)

