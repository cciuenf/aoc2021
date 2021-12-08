"""Functions for getting data from files"""
# import sys
# import os
import importlib
import pandas as pd

def get_daynum(day_number):
    '''Returns the string "daynumber_"'''
    day_str = ''
    if day_number < 10:
        day_str += '0'
    day_str += str(day_number)
    day = 'day'+day_str+'_'
    return day

def get_folder_name(day, folder_name='files'):
    '''returns the folder name'''
    return day + folder_name

def get_datafile_name(day, file_name='data.txt'):
    '''returns the name of the data file'''
    return day+file_name

def get_path(day, middle_char = '/'):
    '''returns the path to read data'''
    return get_folder_name(day)+middle_char+get_datafile_name(day)

def get_module_to_import(day):
    '''get module name to be imported'''
    folder_name = get_folder_name(day)
    file_name = day+'solution'
    module_to_import = folder_name+'.'+file_name
    return module_to_import

def get_imported_package(day):
    '''returns the object(?) of a file that has the functions part1 and part2'''
    module_to_import = get_module_to_import(day)
    imported_module = importlib.import_module(module_to_import)
    return imported_module

def clean_data(data):
    """function to clean the dataframe from pandas"""
    data_list = data.values.tolist()
    cleaned_list = []
    for elem in data_list:
        cleaned_list.append(elem[0])
    return cleaned_list

def get_data(day_number):
    """Function to return the vector of the data"""
    path = get_path(day_number)
    received_data = pd.read_csv(path, header=None)
    cleaned_data = clean_data(received_data)
    return cleaned_data

def challenge_of_the_day(day_number):
    '''Executes the functions from a file of the day received'''
    day = get_daynum(day_number)
    data = get_data(day)
    daily_func = get_imported_package(day)
    daily_func.part1(data)
    daily_func.part2(data)

def spaces(num=3):
    '''Just spacing things n times'''
    print(num*"\n")

def main (day_number=1):
    '''Main function calling the challenge day function spaced out'''
    spaces()
    challenge_of_the_day(day_number)
    spaces()

if __name__ == '__main__':
    main()
