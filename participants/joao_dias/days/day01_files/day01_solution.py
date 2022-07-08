'''This is the script for Advent of Code 2021
https://adventofcode.com/2021/day/1 '''

def part1(data):
    ''' compares the values of an element and its previous value
        if element is bigger, adds one to a counter'''
    number_of_increments = 0
    for i in range(1,len(data)):
        if data[i] > data[i-1]:
            number_of_increments+=1
    print(number_of_increments)

def part2(data):
    ''' compares the values of the sum of 3 element and its previous sum
        if sum is bigger, adds one to a counter'''
    number_of_increments = 0
    i=3
    old_sum = data[i-3] + data[i-2] + data[i-1]
    for i in range (3,len(data)):
        new_sum = data[i-2] + data[i-1] + data[i-0]
        if new_sum > old_sum:
            number_of_increments += 1
        old_sum = new_sum
    print (number_of_increments)
