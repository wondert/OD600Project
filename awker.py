# -*- coding: utf-8 -*-
"""
This module emulates the Unix awk utility's ability to strip a specific 
column out of a file and return that column as a list.
The module contains two functions: awker4csv and awker4excel. These functions
extract a specific column from a .csv or .xlsx file and return it as a list
"""
# xlrd required for awker4excel
import xlrd

def awker4csv(file, col, platetype):
    '''
    platetype = 2 for plates with control wells, 1 if half control wells, 
    0 if no control wells
    col = column of interest, assumes indexed from 1
    awker4csv('path', col#, 0) for plate with no control wells, data from col#
    '''        
    filename = r'{}'.format(file)    
    worms = [line.rstrip().split(',')[col - 1] for line in open(filename)]
    worms_per_well = []    
    for x in worms:
        try:
            num = 0            
            if x:
                if x != 'x':
                    num = int(x)
                elif x == 'x':
                    num = 'x'
        except: 
            continue
        else:
            if num < 30 or num == 'x':            
                worms_per_well.append(num)
    # reading csv files using open will remove empty fields 
    if platetype == 2:
        return worms_per_well[1:91]
    elif platetype == 1:
        return worms_per_well[1:94]
    elif platetype == 0:
        return worms_per_well[1:97]
        
        
def awker4excel(file, col, tab, platetype):
    '''
    platetype = 2 for plates with control wells, 1 if half control wells, 
    0 if no control wells
    col = column of interest, assumes indexed from 0
    tab = excel sheet/tab (0 for first tab, 1 for second etc.) 
    awker4excel('path', col#, 0, 0) for plate with no control wells data, data in col# on the first tab 
    '''        
    filename = r'{}'.format(file)
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_index(tab)    
    worms_per_well = [sheet.cell_value(row, col) for row in range(sheet.nrows)][3:99]
    worms = []    
    if platetype == 2:
        offsets = [x for x in range(96) if (x + 1) % 8 != 0]
        for x in offsets:
            i = worms_per_well[x]
            worms.append(i)
        return worms
    elif platetype == 1:
        offsets = [x for x in range(48) if (x + 1) % 8 != 0]
        # offsets.insert(42, 47)         
        for x in offsets:
            i = worms_per_well[x]
            worms.append(i)
        return worms + worms_per_well[48:]
    elif platetype == 0:
        return worms_per_well

# import os 

# os.chdir(r'C:\Users\Rafael\Pybio\OD600Project')

# from awker import awker4excel

# x = awker4excel('plate_6controlwells.xlsx', 10, 0, 1)
 