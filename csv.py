import csv
with open('D:\python\Things.csv','r')as file:
	reader=csv.reader(file,delimiter='\t')
	for row in reader:
		print(row[0])