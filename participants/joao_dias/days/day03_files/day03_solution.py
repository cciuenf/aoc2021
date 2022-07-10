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
    def multiply_binary (bin_1, bin_2):
        return int(bin_1, 2) * int(bin_2, 2)
    new_data_set = get_new_data_set(data)
    frequencies = get_frequency_of_1s (new_data_set)
    gamma, epsilon = get_gamma_epsilon (frequencies)
    p1_solution = multiply_binary (gamma, epsilon)
    return p1_solution

def part2(data):
    '''Day 03, Part 2 - 33min37'''
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

    def get_common_digits_from_list (data):
        num_of_1 = data.count('1')
        value_to_return = ['1','0']
        if num_of_1 >= len(data)/2 :
            value_to_return = ['0','1']
        return value_to_return

    def get_all_digits_from_column_n (data, column_number):
        digits = []
        for elem in data:
            digits.append(elem[column_number])
        return digits

    def pluck_common_digit_from_index_of_data (most_common, index, data):
        n_data = []
        for elem in data:
            if elem[index] == most_common:
                n_data.append(elem)
        return n_data

    def get_ratings (n_data, most_or_least):
        index = 0
        while(len(n_data) != 1 or index > 13):
            digits = get_all_digits_from_column_n(n_data, index)
            common = get_common_digits_from_list(digits)
            n_data = pluck_common_digit_from_index_of_data (common[most_or_least], index, n_data)
            index += 1
        return n_data[0]

    def multiply_binary (bin_1, bin_2):
        return int(bin_1, 2) * int(bin_2, 2)

    n_data = get_new_data_set(data)
    oxygen_generator_rating = get_ratings (n_data,0)
    co2_scrubber_rating = get_ratings (n_data,1)
    print(oxygen_generator_rating, co2_scrubber_rating)
    p2_solution = multiply_binary (oxygen_generator_rating, co2_scrubber_rating)
    return p2_solution
