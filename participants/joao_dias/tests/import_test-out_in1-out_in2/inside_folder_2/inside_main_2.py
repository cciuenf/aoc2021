'''INSIDE MAIN'''
import inside_file_2 as inside_functions_2

def spaces():
    '''Just spacing things out'''
    print(3*"\n")

def main ():
    """Main function calling the challenge day function"""
    spaces()
    print("inside main")
    inside_functions_2.inside2_func1()
    inside_functions_2.inside2_func2()
    spaces()

if __name__ == '__main__':
    main()
