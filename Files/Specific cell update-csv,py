import csv
with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Contribution"])
    writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
    writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
    writer.writerow([3, "Guido van Rossum", "Python Programming"])
    file.close()
with open('innovators.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    mylist = list(reader)
    file.close()

    mylist[1][0] = 22
with open('innovators.csv', 'w', newline='') as new_file:

    writer = csv.writer(new_file)
    writer.writerows(mylist)
    new_file.close()
    
    
#Data:
    
#SN,Name,Contribution
#22,Linus Torvalds,Linux Kernel
#2,Tim Berners-Lee,World Wide Web
#3,Guido van Rossum,Python Programming
