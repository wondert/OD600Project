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
    experiment_name = [filesinfolder_day1, filesinfolder_day4]
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