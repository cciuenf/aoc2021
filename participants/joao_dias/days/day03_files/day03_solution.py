'''This is the script for Advent of Code 2021
https://adventofcode.com/2021/day/3 '''

def part1(data):
    '''Day 03, Part 1 - Xmin01'''
    max_size = 0
    for elem in data:
        max_size = len(str(elem)) if len(str(elem)) > max_size else max_size
    temp_elems = []
    for elem in data:
        temp_array = []
        for char in str(elem):
            temp_array.append(char)
        temp_elems.append(temp_array)

    print(temp_elems)

    print(max_size)
    print(123456)

def part2(data):
    '''Day 03, Part 2 - Xmin'''
    print(123456)
