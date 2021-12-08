'''INSIDE MAIN'''
import inside_file_1 as inside_functions_1

def spaces():
    '''Just spacing things out'''
    print(3*"\n")


def main ():
    """Main function calling the challenge day function"""
    spaces()
    print("inside main")
    inside_functions_1.inside1_func1()
    inside_functions_1.inside1_func2()
    spaces()

if __name__ == '__main__':
    main()
