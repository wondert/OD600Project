'''
Created on Sep 8, 2014

@author: rgomezam
'''
'''
Import glob module to extract file names from a folder
'''
import glob

'''
Function that places all file names in a folder into a list
'''
def folder_list_maker(filepath_day1, filepath_day4, experiment_name):
    '''
    Defined arguments for glob.glob method with regular expression to find .txt files 
    '''
    path_day1 = filepath_day1 + "/*.txt"
    path_day4 = filepath_day4 + "/*.txt"
    '''
    Extract files from folder and assign to list
    '''
    filesinfolder_day1 = glob.glob(path_day1)
    filesinfolder_day4 = glob.glob(path_day4)
    files_in_day1 = len(filesinfolder_day1)
    files_in_day4 = len(filesinfolder_day4)  
    print("Experiment: " + experiment_name)
    print("No. Files in Day 1: " + str(files_in_day1))
    print("No. Files in Day 4: " + str(files_in_day4))
    # sorts file names for each list, then zips ordered lists together    
    experiment_name = zip(filesinfolder_day1.sorted(), filesinfolder_day4.sorted())
    # experiment_name = [filesinfolder_day1, filesinfolder_day4]
    return experiment_name
'''
test commands to be placed inside folder_list_maker function
print(len(filesinfolder_day1))
print(len(filesinfolder_day4))
'''

'''
Test commands to check if function and module

experiment_name = input("Enter Name of Experiment: ")
filepath_day1 = input("Enter Absolute Path to Folder With Day 1 Data: ")
filepath_day4 = input("Enter Absolute Path to Folder With Day 4 Data: ")
folder_list_maker(filepath_day1, filepath_day4, experiment_name)
'''

# File is stored in Western (Mac OS Roman) encoding aka 'macintosh', convert to UTF-8 for manipulation with codecs package
import codecs
def OD600values(zippedfilepaths):
    '''
    Returns dict with plate# as keys and two lists with the OD600 measurements 
    for day1 and day 4 as a tuple (day1, day4) for the values
    '''     
    correctedpaths = []  
    ordered_plate_list = []
    for x, y in zippedfilepaths:
        day1_path = r'{}'.format(x)
        day4_path = r'{}'.format(y)
        correctedpaths.append((day1_path, day4_path))
        ordered_plate_list.append(day1_path[-13, -11])        
    OD600measurements = {}
    counter = 0
    for day1, day4 in correctedpaths:
        # Used a generator statement in list comprehension to read in file by line and line contents by tab (\t)
        # Used codecs.open method to have 'macintosh' encoded file open and read in utf-8 encoding
        OD600file_d1 = [line.split('\t') for line in codecs.open(day1, 'rU', 'macintosh')]
        OD600file_d4 = [line.split('\t') for line in codecs.open(day4, 'rU', 'macintosh')]
        # Convert actual measurements into floats with list comprehension
        OD600_d1 = [float(number) for number in OD600file_d1[6][2:-1]]
        OD600_d4 = [float(number) for number in OD600file_d4[6][2:-1]]
        OD600measurements[ordered_plate_list[counter]] = (OD600_d1, OD600_d4)
        counter += 1
    return OD600measurements