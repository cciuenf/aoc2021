'''This is the script for Advent of Code 2021
https://adventofcode.com/2021/day/3 '''

def part1(data):
    '''Day 03, Part 1 - 52min24+'''
    def get_called_numbers(data):
        first_line = str(data[0])
        first_line_no_new_line = first_line.replace('\n','')
        called_numbers = first_line_no_new_line.split(',')
        # should I convert them all into int?
        return called_numbers
    def get_tables(data):
        def remove_occurrances_in_list (data, character):
            new_data = []
            for elem in data:
                if elem != character:
                    new_data.append(elem)
            return new_data
        def split(list_a, chunk_size):
            for i in range(0, len(list_a), chunk_size):
                yield list_a[i:i + chunk_size]

        new_data = data[2:]
        new_data = remove_occurrances_in_list(new_data, '\n')
        new_list = list(split(new_data, 5))
        new_tables = []
        for table in new_list:
            new_table = []
            for cell in table:
                s_cell = str(cell)
                s_cell = s_cell.replace('\n', ' ')
                num_list = s_cell.split(' ')
                new_cell = remove_occurrances_in_list(num_list, '')
                new_table.append(new_cell)
            new_tables.append(new_table)
        return new_tables

    def mark_number(tables, called_number):
        for table in tables:
            for row in table:
                for elem in row:
                    if elem == called_number:
                        
#    def has_completed_rows(table):
#        pass
#    def has_completed_columns(table):
#        pass
#    def has_won(table):
#        pass
#    def sum_remainder_cells(table):
#        pass
    called_number_list = get_called_numbers(data)
    tables = get_tables(data)
    for called_number in called_number_list:
        mark_number(tables, called_number)
    # print(data)

def part2(data):
    '''Day 03, Part 2 - min'''
    return 0
