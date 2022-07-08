'''This is the script for Advent of Code 2021
https://adventofcode.com/2021/day/2 '''

def part1(data):
    '''Day 02, Part 1 - 5min01'''
    horizontal_position = 0
    depth = 0
    for elem in data:
        splitted = elem.split(' ')
        command = splitted[0]
        splitted_value = int(splitted[1])
        if command == 'forward':
            horizontal_position += splitted_value
        if command == 'up':
            depth -= splitted_value
        if command == 'down':
            depth += splitted_value
    print(horizontal_position*depth)

def part2(data):
    '''Day 02, Part 2 - 3min'''
    aim = 0
    horizontal_position = 0
    depth = 0
    for elem in data:
        splitted = elem.split(' ')
        command = splitted[0]
        splitted_value = int(splitted[1])
        if command == 'forward':
            depth += splitted_value*aim # It increases your depth by your aim multiplied by X
            horizontal_position += splitted_value   # increases your horizontal position by X
        elif command == 'up':
            aim -= splitted_value                       # up X decreases your aim by X
        elif command == 'down':
            aim += splitted_value                       # down X increases your aim by X
    print(horizontal_position*depth)
