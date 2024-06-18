import csv

with open("C:/Users/Satakshi Wadhwa/OneDrive/Desktop/customers-100.csv",'r') as file:
    csvreader=csv.reader(file)
for row in csvreader:
    print(row)



