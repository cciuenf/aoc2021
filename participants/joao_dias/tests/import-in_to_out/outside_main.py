'''OUTSIDE MAIN'''
import inside_folder.inside_file as inside_functions
import outside_file as outside_functions


def main ():
    """Main function calling the challenge day function"""
    print("outside main")
    inside_functions.f_inside1()
    outside_functions.f_outside1()

if __name__ == '__main__':
    main()
