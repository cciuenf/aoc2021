'''This is the script for Advent of Code 2021
https://adventofcode.com/2021/day/2 '''

def part1(data):
    '''Day 02, Part 1 - 5min01'''
    distance = 0
    depth = 0
    for elem in data:
        splitted = elem.split(' ')
        command = splitted[0]
        splitted_value = int(splitted[1])
        if command == 'forward':
            distance += splitted_value
        if command == 'up':
            depth -= splitted_value
        if command == 'down':
            depth += splitted_value
    print(distance*depth)

def part2(data):
    '''Day 02, Part 2 - 3min'''
    aim = 0
    distance = 0
    depth = 0
    for elem in data:
        splitted = elem.split(' ')
        command = splitted[0]
        splitted_value = int(splitted[1])
        if command == 'forward':
            distance += splitted_value
            depth += splitted_value*aim
        elif command == 'up':
            depth -= splitted_value
            aim -= splitted_value
        elif command == 'down':
            depth += splitted_value
            aim += splitted_value
    print(distance*depth)
