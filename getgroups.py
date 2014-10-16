'''
This module takes data from a list and groups it. Will be useful for after dxOD600/XO values calculated
for use with matplotlib for data analysis.

Still need to correct getdata function, this is just a template for ETL.
'''
# getrange has been successfully debugged (see code below)
def getrange(groupsize):
	data_counters = list(zip(range(0, 12, groupsize), range(groupsize, 12 + groupsize, groupsize)))
	rangelist = [list(zip(range(x, 96, 12), range(y, 96, 12))) for (x, y) in data_counters]
	return rangelist

# this code needs to be debugged, tuple unpacking assignment error in for loop
def getdata(data, rangelist):
	list = [[] for i in range(len(rangelist))]
	for item, i in rangelist, range(len(rangelist)):
		group = [list[i].append(data[x:y]) for x, y in item]
	return group
	
	
'''	
### This code highlights the dangers of working with list comps, iterators, and generators.

def getrange(groupsize):
	# generators and iterators are lazy and need to be explicitly called, so need list() instead of [zip(x,y)] 
	data_counters = [zip(range(0, 12, groupsize), range(groupsize, 12 + groupsize, groupsize))]
	# if above was not corrected, we would get tuple assignment error
	# expected values to unpack(2)... too many value to unpack
	total = [list(zip(range(x, 96, 12), range(y, 96, 12))) for x, y in data_counters]
	return total

def getdata(data):
	list = []
	group = [list.extend(data(x:y) for item in total for x, y in item]
	return group
	
'''
# Use the below as test code for both functions (maybe think of better fakedata set).
'''
x = getrange(3)	
print(getrange(3))
fakedata = list(range(96))	
results = getdata(fakedata, x)
print(results)
'''