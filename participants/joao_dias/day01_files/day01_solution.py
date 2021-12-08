"""This is the script for Advent of Code 2021
https://adventofcode.com/2021/day/1
"""
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
