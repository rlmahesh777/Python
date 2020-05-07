# importing the csv module
import csv

# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']

# data rows of csv file
rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]

# name of csv file
filename = "university_records.csv"

# writing to csv file
with open(filename, 'w', newline= '') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)
    # writing the data rows
    csvwriter.writerows(rows)
    # closing the file
    csvfile.close()
with open(filename, 'r', newline= '') as csvfile:
    # creating a csv writer object
    csvreader = csv.reader(csvfile)
    # converting reader object into list
    records_list = list(csvreader)
    for row in records_list:
       print(row)

    # closing the csvfile
       csvfile.close()

    # input to the file
    records_list[2][2] = 6
with open(filename, 'w', newline= '') as new_csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(new_csvfile)

    # writing the fields
    csvwriter.writerow(fields)
    # writing the data rows
    csvwriter.writerows(rows)
    for row in records_list:
     print(row)
    # closing the file
     new_csvfile.close()



