"""This is the script for Advent of Code 2021
https://adventofcode.com/2021/day/1
"""
import pandas as pd
def clean_data(data):
    """function to clean the dataframe from pandas"""
    data_list = data.values.tolist()
    cleaned_list = []
    for elem in data_list:
        cleaned_list.append(elem[0])
    return cleaned_list

def get_data():
    """Function to return the vector of the data"""
    # cleaned_data = [199,200,208,210,200,207,240,269,260,263]
    received_data = pd.read_csv("day01_files/day01_data.txt", header=None)
    cleaned_data = clean_data(received_data)
    return cleaned_data

def part1(data):
    """This return the number of data that are bigger than previous"""
    previous_value = -1
    number_of_increments = 0
    for elem in data:
        if (elem > previous_value) and (previous_value != -1):
            number_of_increments+=1
        previous_value = elem
    print(number_of_increments)

def part2(data):
    """Prints the number of interval increments"""
    previous_sum = -1
    number_of_increments = 0
    # for i in range (len(data)):
    # for i, _ in enumerate(data):
    for i, elem in enumerate(data):
        if i<=len(data)-3:
            new_sum = elem+data[i+1]+data[i+2]
            #new_sum = data[i]+data[i+1]+data[i+2]
            if i == 0:
                previous_sum = new_sum
            elif new_sum > previous_sum:
                number_of_increments += 1
            previous_sum = new_sum
    print (number_of_increments)

def day1():
    """Challenge day one"""
    data = get_data()
    # part1(data)
    part2(data)

def spaces():
    '''Just Spacing things'''
    print("\n\n\n\n")

def main ():
    """Main function calling the challenge day function"""
    spaces()
    day1()
    spaces()

if __name__ == '__main__':
    main()
