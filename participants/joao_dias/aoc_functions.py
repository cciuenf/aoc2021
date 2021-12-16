"""Functions for getting data from files"""
# import sys
# import os
import importlib
import pandas as pd
# import xlrd             # Reading an excel file using Python

def get_daynum(day_number, day_prefix='day', terminator='_'):
    ''' receives:   a numeric value that refers to the day
                    the prefix of the day
                    a terminator character
        returns:    a string "day"+number+"terminator" '''
    day_str = ''
    if day_number < 10:
        day_str += '0'
    day_str += str(day_number)
    day = day_prefix+day_str+terminator
    return day

def get_path(day_number, middle_char, file_sufix, folder_sufix='files'):
    ''' receives:   a numeric value that refers to the day
                    the middle char that separates folder and datafile names
                    the sufix of the file containing informations
                    the sufix of the folder that contains the info of a day-challenge
        returns:    the path to read data'''
    day = get_daynum(day_number)
    return day+folder_sufix+middle_char+day+file_sufix

def get_imported_package(day_number, middle_char = '.', file_sufix = 'solution'):
    ''' receives:   a numeric value that refers to the day
                    the middle char that separates folder and datafile names
                    the sufix of the file containing the functions
        returns:    the object(?) of a file that has the functions part1 and part2'''
    module_to_import = get_path(day_number, middle_char, file_sufix)
    imported_module = importlib.import_module(module_to_import)
    return imported_module

def dataframe_to_list(dataframe_from_pandas):
    ''' receives:   a dataframe from pandas
        returns:    the data in a list'''
    dataframe_list = dataframe_from_pandas.values.tolist()
    cleaned_list = []
    for elem in dataframe_list:
        cleaned_list.append(elem[0])
    return cleaned_list

def get_data(day_number=0, middle_char = '/', file_sufix = 'data.txt'):
    ''' receives:   a numeric value that refers to the day
                    the middle char that separates folder and datafile names
                    the sufix of the file containing data
        returns:    a list of data'''
    path = get_path(day_number, middle_char, file_sufix)
    dataframe_from_pandas = pd.read_csv(path, header=None)
    data_list = dataframe_to_list(dataframe_from_pandas)
    return data_list

def reading_answers_from_excel(day_number, path='solutions.xlsx'):
    ''' receives:   a numeric value that refers to the day
                    path to the excel file
        returns:    nothing
    '''
    sheet_number = 2*day_number - 2
    result_list = []
    workbook = pd.read_excel(path, header=None, sheet_name=sheet_number)
    lista = dataframe_to_list(workbook)
    result_list.append(int(lista[0]))
    sheet_number += 1
    workbook = pd.read_excel(path, header=None, sheet_name=sheet_number)
    lista = dataframe_to_list(workbook)
    result_list.append(int(lista[0]))
    return result_list

def print_results(excel_results, data, day_number, daily_func):
    '''Prints the results from code and Excel'''
    print('D'+str(day_number)+'P1 (Code ):  ', end='')
    daily_func.part1(data)
    print('D'+str(day_number)+'P1 (Excel):  ', end='')
    print(excel_results[0])
    print('D'+str(day_number)+'P2 (Code ):  ', end='')
    daily_func.part2(data)
    print('D'+str(day_number)+'P2 (Excel):  ', end='')
    print(excel_results[1])

def challenge_of_the_day(day_number):
    ''' receives:   a numeric value that refers to the day challenge
        and then executes the functions from this day's challenge'''
    data = get_data(day_number)
    daily_func = get_imported_package(day_number)
    excel_results = reading_answers_from_excel(day_number)
    print_results(excel_results, data, day_number, daily_func)

def spaces(number_of_spaces=3):
    ''' receives:   the number of spaces to have
        then:       prints "\\n" n times'''
    print(number_of_spaces*'\n')

def main(day_number=2):
    '''spaces the print on terminal and calls the challenge of the day'''
    spaces()
    challenge_of_the_day(day_number)
    spaces()

if __name__ == '__main__':
    main()
