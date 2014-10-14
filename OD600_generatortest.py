# File is stored in Western (Mac OS Roman) encoding aka 'macintosh', convert to UTF-8 for manipulation with codecs package
import codecs
# Used a generator statement in list comprehension to read in file by line and line contents by tab (\t)
# Used codecs.open method to have 'macintosh' encoded file open and read in utf-8 encoding
OD600file = [line.split('\t') for line in codecs.open('/Users/rgomezam/OD600_template.txt', 'rU', 'macintosh')]
# Convert actual measurements into floats with list comprehension
OD600measurements = [float(number) for number in OD600file[6][2:-1]]
print(OD600measurements)

