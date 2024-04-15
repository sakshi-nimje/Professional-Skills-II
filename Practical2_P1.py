import pandas as pd
import requests
import csv

txt_path='perimeter.txt'
csv_path='cars.csv'
txt_url='https://sample-files-nu.vercel.app/sherlock.txt'
csv_url='https://gist.githubusercontent.com/bobbyhadz/9061dd50a9c0d9628592b156326251ff/raw/381229ffc3a72c04066397c948cf386e10c98bee/employees.csv'

# Opening TXT file from Disk
perimeter=open(txt_path,'r')
print("Txt File from Disk:  ")
print('-------------------------------------------------------------------')
print(perimeter.read())
# Opening CSV file from Disk
cars=pd.read_csv(csv_path)
print("CSV File from Disk:  ")
print('-------------------------------------------------------------------')
print(cars.head())
# Opening TXT file from Web
response = requests.get(txt_url)
peri = response.text
print("Txt File from Web:  ")
print('-------------------------------------------------------------------')
print(peri)
# Opening CSV file from Web
data = pd.read_csv(csv_url,sep=',',encoding='utf-8',)
print("CSV File from Web:  ")
print('-------------------------------------------------------------------')
print(data.head())
print('\n')

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
with open(filename, 'w') as csvfile:
	# creating a csv writer object
	csvwriter = csv.writer(csvfile)
	# writing the fields
	csvwriter.writerow(fields)
	# writing the data rows
	csvwriter.writerows(rows)
print(f"The data has been writteen in the CSV File named {filename} !!")
