import csv

file = input()

amountWords = {}

with open(file, 'r') as csvfile:
   csvreader = csv.reader(csvfile)
   for row in csvreader:
       for word in row:
           if word not in amountWords.keys():
               amountWords[word] = 1
           else:
               amountWords[word] += 1

for key in amountWords.keys():
   print(key + " " + str(amountWords[key]))
