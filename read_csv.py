

PATH = "/home/judy/Documents/test.csv"

import csv
with open(PATH, 'r') as file:  #using rb gets error: iterator should return strings, not bytes (did you open the file in text mode?)
    content = csv.reader(file)

    for row in content:
        print(row)