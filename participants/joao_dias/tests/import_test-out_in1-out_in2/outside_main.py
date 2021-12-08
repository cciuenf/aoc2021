'''OUTSIDE MAIN'''
import inside_folder_1.inside_file_1 as inside_functions_1
import inside_folder_2.inside_file_2 as inside_functions_2
import importlib

def spaces(num=3):
    '''Just spacing things out'''
    print(num*".\n")

def method1():
    '''Importing "Normally" '''
    print('Importing "Normally"')
    inside_functions_1.inside1_func1()
    inside_functions_1.inside1_func2()
    inside_functions_2.inside2_func1()
    inside_functions_2.inside2_func2()

def method2():
    '''Importing with variable'''
    path_1 = 'inside_folder_1'
    # path_2 = 'inside_folder_2'
    # print(path_1, '\n',path_2)
    file_name_1 = 'inside_file_1'
    # file_name_2 = 'inside_file_2'

    # # It is possible to use the __import__ function to import using a variable.
    # package = "os"
    # name = "path"
    # imported = getattr(__import__(package, fromlist=[name]), name)
    # # is equivalent to
    # from os import path as imported
    # imported = il.import_module("package.path.%s" % module_name)
    imported = importlib.import_module(path_1+'.'+file_name_1)
    imported.inside1_func1()

def get_day_import(number):
    '''returns the object(?) of a file that has the functions'''
    str_number = str(number)
    path = 'inside_folder_'+ str_number
    file_name = 'inside_file_'+ str_number
    module_to_import = path+'.'+file_name
    imported_1 = importlib.import_module(module_to_import)
    return imported_1

def method3(number):
    '''is it right now?'''
    day = get_day_import(number)
    day.func1()
    day.func2()


def main ():
    """Main function calling the challenge day function"""
    print("outside main")
    # spaces(2)
    # method1()
    spaces(2)
    # method2()
    method3(2)

if __name__ == '__main__':
    spaces()
    main()
    spaces()
