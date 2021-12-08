'''OUTSIDE MAIN'''

def spaces(num=3):
    '''Just spacing things out'''
    print(num*".\n")

def func():
    '''Importing with variable'''
    x_1 = 2
    if x_1>2:
        print('hey')

def main ():
    """Main"""
    spaces(2)
    func()
    spaces(2)

if __name__ == '__main__':
    spaces()
    main()
    spaces()
