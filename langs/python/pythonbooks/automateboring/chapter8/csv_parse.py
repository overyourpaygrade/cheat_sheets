import csv

print "\nExample 1 - Reader Objects"
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

#print exampleData
'''
[['4/5/2014 13:34', 'Apples', '73'], ['4/5/2014 3:41', 'Cherries', '85'], ['4/6/2014 12:46', 'Pears', '14'], ['4/8/2014 8:59', 'Oranges', '52'], 
['4/10/2014 2:07', 'Apples', '152'], ['4/10/2014 18:10', 'Bananas', '23'], ['4/10/2014 2:40', 'Strawberries', '98']]
'''

print exampleData[0][0]
'''4/5/2014 13:34'''

print exampleData[0][1]
'''Apples'''

print exampleData[0][1]
'''Cherries'''

print exampleData[1][1]
'''73'''

print exampleData[6][1]
'''Strawberries'''

print "\nExample 2 - Reading data from reader objects in a for loop"

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
  print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
'''
Row #1 ['4/5/2014 13:34', 'Apples', '73']
Row #2 ['4/5/2014 3:41', 'Cherries', '85']
Row #3 ['4/6/2014 12:46', 'Pears', '14']
Row #4 ['4/8/2014 8:59', 'Oranges', '52']
Row #5 ['4/10/2014 2:07', 'Apples', '152']
Row #6 ['4/10/2014 18:10', 'Bananas', '23']
Row #7 ['4/10/2014 2:40', 'Strawberries', '98']
'''

print "\nExample 3 - Writer objects"
outputFile = open('output.csv', 'w')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam','eggs','bacon','ham'])
outputWriter.writerow(['Hello world!','eggs','bacon','ham'])
outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()

'''
spam,eggs,bacon,ham
Hello world!,eggs,bacon,ham
1,2,3.141592,4
'''

print "\nExample 4 - The delimiter and lineterminator keyword args"
csvFile = open('example.tsv', 'w')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['apples','oranges','grapes'])
csvWriter.writerow(['eggs','bacon','ham'])
csvWriter.writerow(['spam','spam','spam','spam','spam','spam'])
csvFile.close()

