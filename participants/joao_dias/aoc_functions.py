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
    day_str = '0' if day_number < 10 else ''
    day_str += str(day_number)
    day = day_prefix+day_str+terminator
    return day

def get_path(day_number, middle_char, file_sufix, folder_sufix='files', parent_folder= 'days'):
    ''' receives:   a numeric value that refers to the day
                    the middle char that separates folder and datafile names
                    the sufix of the file containing informations
                    the sufix of the folder that contains the info of a day-challenge
        returns:    the path to read data'''
    day = get_daynum(day_number)
    # return day+folder_sufix+middle_char+day+file_sufix
    return parent_folder+middle_char+day+folder_sufix+middle_char+day+file_sufix

def get_imported_package(day_number, middle_char = '.', file_sufix = 'solution'):
    ''' receives:   a numeric value that refers to the day
                    the middle char that separates folders and datafile names
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
    def get_excel_answer (sheet_number):
        workbook = pd.read_excel(path, header=None, sheet_name=sheet_number)
        lista = dataframe_to_list(workbook)
        answer = int(lista[0])
        return answer

    sheet_number = 2*day_number - 2
    part1 = get_excel_answer(sheet_number)
    part2 = get_excel_answer(sheet_number+1)
    return [part1, part2]

def reading_answers_from_python(day_number, data):
    '''Centralized function to get python solutions'''
    daily_func = get_imported_package(day_number)
    part1 = daily_func.part1(data)
    part2 = daily_func.part2(data)
    return [part1, part2]

def get_results (day_number, data):
    ''' Centralized function to get all results from data and structure them '''
    excel_results = reading_answers_from_excel(day_number)
    python_results = reading_answers_from_python(day_number, data)
    results = {
        'P1': {
            'Python': python_results[0],
            'Excel': excel_results[0],
        },
        'P2': {
            'Python': python_results[1],
            'Excel': excel_results[1],
        },
    }
    return results

def print_results(day_number, results):
    '''Prints the results from code and Excel'''
    day = str(day_number)
    print('D'+day+'P1 (Code ):  ', results['P1']['Python'])
    print('D'+day+'P1 (Excel):  ', results['P1']['Excel' ])
    print('D'+day+'P2 (Code ):  ', results['P2']['Python'])
    print('D'+day+'P2 (Excel):  ', results['P2']['Excel' ])

def challenge_of_the_day(day_number):
    ''' receives:   a numeric value that refers to the day challenge
        and then executes the functions from this day's challenge'''
    data = get_data(day_number)
    results = get_results(day_number, data)
    print_results(day_number, results)

def spaces(number_of_spaces=3):
    ''' receives:   the number of spaces to have
        then:       prints "\\n" n times'''
    print(number_of_spaces*'\n')

def main(day_number=3):
    '''spaces the print on terminal and calls the challenge of the day'''
    spaces()
    challenge_of_the_day(day_number)
    spaces()

if __name__ == '__main__':
    main()
