import csv
fc = open('data.csv','r')
list_Data = csv.reader(fc)

lstdata = []
for i in list_Data:
    lstdata.append(i)
print(lstdata)

def read_csv( fn ):
 import csv
 fc = open(fn,'r')
 list_Data = list(csv.reader(fc), encoding = 'utf8')
 return list_Data

my_list = read_csv('test.csv')
print(my_list)