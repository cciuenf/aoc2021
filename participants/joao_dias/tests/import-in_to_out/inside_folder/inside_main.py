'''INSIDE MAIN'''
import inspect
import os
import sys
import inside_file as inside_functions

def spaces():
    '''Just spacing things out'''
    print(3*"\n")


def main ():
    """Main function calling the challenge day function"""
    spaces()
    print("inside main")
    inside_functions.f_inside1()
    inside_functions.f_inside2()
    spaces()

    current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    print(current_dir,"\n")
    parent_dir = os.path.dirname(current_dir)
    print(parent_dir,"\n")
    sys.path.insert(0, parent_dir)
    # print()

    import outside_file as outside_functions

    outside_functions.f_outside1()
    outside_functions.f_outside2()

    spaces()

if __name__ == '__main__':
    main()
