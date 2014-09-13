'''
Created on Sep 12, 2014

@author: rgomezam
'''
from future import division
location_1 = input('Enter path for first measurement:')
location_2 = input('Enter path for second measurement:')
location_3 = input('Enter path for XO counts:')
experiment = input('Experiment Name:')
plate = input('Plate Number:')
type = input('Enter 0 for Plate With Correction Wells. Enter 1 for Plates Without Correction Wells.')
day = input('Age of Worms at final OD600 measurement (L4 = D0):')
date = input('Experiment date (DDMMYY):')
names = list(experiment, plate, type, day)
label = '{}_{}_{}_{}'.format(date, experiment, plate, day)
correct_location_1 = 'r' + location_1
correct_location_2 = 'r' + location_2
correct_location_3 = 'r' + location_3
# open specified file as a file object f
f_1 = open(correct_location_1)
f_2 = open(correct_location_2)
f_3 = open(correct_location_3)
# read file contents split by delimiter
# '\t' will be used by default, tab is the only whitespace delimiter in file
raw_data_1 = f_1.read().split()
raw_data_2 = f_2.read().split()
# XO files will need to be .csv type
raw_data_3 = f_3.read().split(',')
# Code below is specific for output txt files from the SpectraMax
# Well id's (A1-H12) can be indexed at raw_data[17:113]
# Data (A1-H12) can be indexed at  raw_data[114:210]
data1_OD600 = raw_data_1[114:210]
data2_OD600 = raw_data_2[114:210]
data_OD600 = [data2_OD600[i]-data1_OD600[i] for i in range(96)]



# NEED TO PERFORM DIFFERENCE CALCULATION + NORMALIZATION TO NO WORMS + DIVISION BY XO BEFORE NEXT STEP


# DATA ANALYSIS
# Data will be indexed by Plate Type

# Plate without correction wells
if type = 1:
    groupA_1 = data_1[0:3] + data_1[12:15] + data_1[24:27] + data_1[36:39] + data_1[48:51] + data_1[60:63] + data_1[72:75] + data_1[84:87]
    groupB_1 = data_1[3:6] + data_1[15:18] + data_1[27:30] + data_1[39:42] + data_1[51:54] + data_1[63:66] + data_1[75:78] + data_1[87:90]
    groupC_1 = data_1[6:9] + data_1[18:21] + data_1[30:33] + data_1[42:45] + data_1[54:57] + data_1[66:69] + data_1[78:81] + data_1[90:93]
    groupD_1 = data_1[9:12] + data_1[21:24] + data_1[33:36] + data_1[45:48] + data_1[57:60] + data_1[69:72] + data_1[81:84] + data_1[93:]
    groupA_2 = data_2[0:3] + data_2[12:15] + data_2[24:27] + data_2[36:39] + data_2[48:51] + data_2[60:63] + data_2[72:75] + data_2[84:87]
    groupB_2 = data_2[3:6] + data_2[15:18] + data_2[27:30] + data_2[39:42] + data_2[51:54] + data_2[63:66] + data_2[75:78] + data_2[87:90]
    groupC_2 = data_2[6:9] + data_2[18:21] + data_2[30:33] + data_2[42:45] + data_2[54:57] + data_2[66:69] + data_2[78:81] + data_2[90:93]
    groupD_2 = data_2[9:12] + data_2[21:24] + data_2[33:36] + data_2[45:48] + data_2[57:60] + data_2[69:72] + data_2[81:84] + data_2[93:]
# Plate with correction wells
else:
    groupA_1 = data_1[0:3] + data_1[12:15] + data_1[24:27] + data_1[36:39] + data_1[48:51] + data_1[60:63] + data_1[72:75]
    groupB_1 = data_1[3:6] + data_1[15:18] + data_1[27:30] + data_1[39:42] + data_1[51:54] + data_1[63:66] + data_1[75:78]
    groupC_1 = data_1[6:9] + data_1[18:21] + data_1[30:33] + data_1[42:45] + data_1[54:57] + data_1[66:69] + data_1[78:81]
    groupD_1 = data_1[9:12] + data_1[21:24] + data_1[33:36] + data_1[45:48] + data_1[57:60] + data_1[69:72] + data_1[81:84]
    controlA_1 = data_1[84:87] 
    controlB_1 = data_1[87:90] 
    controlC_1 = data_1[90:93] 
    controlD_1 = data_1[93:]
    groupA_2 = data_2[0:3] + data_2[12:15] + data_2[24:27] + data_2[36:39] + data_2[48:51] + data_2[60:63] + data_2[72:75]
    groupB_2 = data_2[3:6] + data_2[15:18] + data_2[27:30] + data_2[39:42] + data_2[51:54] + data_2[63:66] + data_2[75:78]
    groupC_2 = data_2[6:9] + data_2[18:21] + data_2[30:33] + data_2[42:45] + data_2[54:57] + data_2[66:69] + data_2[78:81]
    groupD_2 = data_2[9:12] + data_2[21:24] + data_2[33:36] + data_2[45:48] + data_2[57:60] + data_2[69:72] + data_2[81:84]
    controlA_2 = data_2[84:87] 
    controlB_2 = data_2[87:90] 
    controlC_2 = data_2[90:93] 
    controlD_2 = data_2[93:]
# Data Analysis
# Plates without correction
