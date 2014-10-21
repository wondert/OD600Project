'''
The module scanner opens any tab-delimited file (.txt):
scans the file line by line
inspects each item in the line (delimited by tabs) for a specific condition
if the condition is not met, that line will be written to a new tab-delimited file
if the condition is met, that line will not be written to a new tab-delimited file
The output file will have the identical structure only difference will be presence of a line
'''
import os
t = os.getcwd()
def goback():
	os.chdir(t)
def gowhere():
	print(t)
inputfolder = input('Enter Full Path For Input Folder: ')
inputfile = input('Enter Full Name of Input File: ')
outputfile = input('Enter Name For Output File: ')
col = input('Enter Position to Edit:')
col_i = int(col)
y = input('Enter Condition to Exclude: ')
folderdirectory = r'{}'.format(inputfolder)
os.chdir(folderdirectory)
j = os.getcwd()
print('')
print('x'*60)
print('')
print('You are now working in {}'.format(j))
print('Enter scanner.gowhere() to view previous working directory')
print('Enter scanner.goback() to return your previous working directory')
destination = r'{}.txt'.format(outputfile)
new = open(destination, 'a')
test = r'{}'.format(inputfile)
for line in open(test):
	if line.split()[col_i] != y:
		new.write(line)
new.close()
print('')
print('x'*60)
print('x'*60)
print('')
print('Contents of {}'.format(destination))
counter1 = 0
for line in open(destination):
	if counter1 < 11:
		print(line)
		counter1 = counter1 + 1
print('')
print('x'*60)
print('')
print('Contents of {}'.format(test))
counter2 = 0
for line in open(test): 
	if counter2 < 11:
		print(line)
		counter2 = counter2 + 1

'''
This code works when p10.txt is the input file, and it is in the the current working directory of python
We want to remove any lines (rows) where the value of column 10 = '.' 

new = open('p10_edit.txt', 'a')
for line in open('p10.txt'):
	if line.split()[10] != '.':
		new.write(line)
new.close()

counter1 = 0
for line in open('p10.txt'):
	if counter1 < 11:
		print(line)
		counter1 = counter1 + 1

counter2 = 0
for line in open('p10_edit.txt'): 
	if counter2 < 11:
		print(line)
		counter2 = counter2 + 1
'''
