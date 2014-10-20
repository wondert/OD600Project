# This gives a list of tuples that need to be grouped by the size of the first element in tuple
x = [j for i in range(8) for j in range(1,13)]
y = range(1,97)
z = list(itertools.zip_longest(x,y))

# Want to use the groupby function, take first element in tuple as key to group by
# ??? for k,g in itertools.groupby(t, lambda x: x[0]) for item in g
# Want either a list of lists or a dict, have code that does this need to find start with above