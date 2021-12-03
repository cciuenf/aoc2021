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

def get_sonar_sweep():
    """Function to return the vector of the data"""
    #sweep_vector=[199,200,208,210,200,207,240,269,260,263]
    received_data = pd.read_csv("day1_data.txt", header=None)
    cleaned_data = clean_data(received_data)
    return cleaned_data

def get_number_of_increments(sonar_data):
    """This return the number of data that are bigger than previous"""
    previous_value = -1
    number_of_increments = 0
    for elem in sonar_data:
        if elem>previous_value and previous_value != -1:
            number_of_increments+=1
        previous_value = elem
    return number_of_increments

def get_number_of_interval_increments(data):
    """returns the number of interval increments"""
    previous_sum = -1
    number_of_increments = 0
    #for i in range (len(data)):
    for i, elem in enumerate(data):
        if i<=len(data)-3:
            new_sum = elem+data[i+1]+data[i+2]
            #new_sum = data[i]+data[i+1]+data[i+2]
            if i == 0:
                previous_sum = new_sum
            elif new_sum > previous_sum:
                number_of_increments += 1
            previous_sum = new_sum
    return number_of_increments

def part1(data):
    """Prints the number of increments from data"""
    print(get_number_of_increments(data))

def part2(data):
    """Prints the number of increases from data intervals"""
    print(get_number_of_interval_increments(data))

def day1():
    """Challenge day one"""
    sonar_data = get_sonar_sweep()
    #part1(sonar_data)
    part2(sonar_data)


def main ():
    """Main function calling the challenge day function"""
    day1()

if __name__ == '__main__':
    main()
