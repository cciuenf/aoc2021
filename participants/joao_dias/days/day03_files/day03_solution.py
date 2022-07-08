'''This is the script for Advent of Code 2021
https://adventofcode.com/2021/day/3 '''

def part1(data):
    '''Day 03, Part 1 - 34min16'''
    def get_new_data_set (data):
        max_size = 0
        for elem in data:
            size = len(str(elem))
            max_size = size if size > max_size else max_size
        new_data = []
        for elem in data:
            str_elem = str(elem)
            size = len(str_elem)
            new_elem = (max_size-size)*'0' + str_elem
            new_data.append(new_elem)
        return new_data
    def get_frequency_of_1s (data):
        python_dict = {}
        for j, _ in enumerate (data[0]):
            python_dict[j] = 0
        for _, word in enumerate(data):
            for j, character in enumerate (word):
                python_dict[j] += int(character)
        return python_dict
    def get_gamma_epsilon (frequencies):
        middle = len(data)/2
        gamma = ''
        epsilon = ''
        for item in frequencies.items():
            if item[1] > middle:
                gamma += '1'
                epsilon += '0'
            else:
                gamma += '0'
                epsilon += '1'
        return gamma, epsilon
    new_data_set = get_new_data_set(data)
    frequencies = get_frequency_of_1s (new_data_set)
    gamma, epsilon = get_gamma_epsilon (frequencies)
    dec_g = int(gamma, 2)
    dec_e = int(epsilon, 2)
    print (dec_g * dec_e)

def part2(data):
    '''Day 03, Part 2 - Xmin'''
    print(123456)
