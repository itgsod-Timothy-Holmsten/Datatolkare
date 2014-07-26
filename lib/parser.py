import os

def split_line(line):
    if len(line) == 0:
        raise ValueError('can not parse empty line')

    return line.split()

def encode_line(list):
    if len(list) < 3:
        raise ValueError('incomplete list')

    return {'date': int(list[0]), 'max': int(list[1]), 'min': int(list[2])}

def find_biggest_variation(list):
    if len(list) == 0:
        raise ValueError('list must not be empty')

    compared_value = 0
    compared_dict = dict()
    for compare in list:
        comp = compare['max'] - compare['min']
        if comp > compared_value:
            compared_value = comp
            compared_dict = compare

    return compared_dict

def load_weather_file(path):

    if len(path) == 0:
        raise ValueError('path must not be empty')
    if not os.path.isfile(path):
        raise IOError('file does not exist')

    with open(path, "r") as weather_file:
        weather_data = weather_file.readlines()

    return weather_data[2:]

def main(path):
    weather_data = load_weather_file(path)

    compare_list = []

    for weather in weather_data:
        split = split_line(weather)
        compare_list.append(encode_line(split))

    biggest_variation = find_biggest_variation(compare_list)

    day = biggest_variation['date']
    variation = biggest_variation['max'] - biggest_variation['min']
    str_to_return = 'Day %s had the biggest variation (%.1f degrees)' %(day, variation)

    return str_to_return