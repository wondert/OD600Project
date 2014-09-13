'''
Created on Sep 12, 2014

@author: rgomezam
'''
'''
from future import division
'''
import GetODFiles

experiment_name = input("Enter Name of Experiment: ")
filepath_day1 = input("Enter Absolute Path to Folder With Day 1 Data: ")
filepath_day4 = input("Enter Absolute Path to Folder With Day 4 Data: ")
ODfiles = GetODFiles.folder_list_maker(filepath_day1, filepath_day4, experiment_name)

'''
Test command to check for proper import correct function call
print("Files in folder: " + str(len(ODfiles[0])))
'''