from math import tan, pi
from time import perf_counter


def time_it(fn, *args, repetitions=1, **kwargs):
    """
    :type repetitions: int
    :param fn: This will take specified function name as input
    :param args: This will depend on the function name being passed
    :param repetitions: This parameter represent the count of times the function needs to be run
    :param kwargs: This will depend on the function name being passed
    :return: returns the time taken to execute the function for the number or repetitions
    """
    if type(repetitions) is not int:
        raise TypeError("Repetitions can only be an integer")
    elif repetitions <= 0:
        raise ValueError("Repetitions can only be a non-zero integer")
    elif fn not in ['print', 'squared_power_list', 'polygon_area', 'temp_converter', 'speed_converter']:
        raise ValueError('Not a valid function name')

    start_time = perf_counter()

    for _ in range(repetitions):
        if fn == 'print':
            print(*args, **kwargs)
        elif fn == 'squared_power_list':
            print(f'squared_power_list is', squared_power_list(*args, **kwargs))
        elif fn == 'polygon_area':
            print(f'polygon area is', polygon_area(*args, **kwargs))
        elif fn == 'temp_converter':
            print(f'temperature in celsius is', temp_converter(*args, **kwargs))
        elif fn == 'speed_converter':
            print(f'converted speed is', speed_converter(*args, **kwargs))

    end_time = perf_counter()

    avg_time = (end_time - start_time) / repetitions

    print(f'the average time taken for {fn}:', avg_time)

    return avg_time


def squared_power_list(num, start, end):
    """
    :param num: number that is to be taken power of
    :param start: starting power
    :param end: ending power
    :return: list of powers
    """
    if type(num) is not int:
        raise TypeError("The number provided is not integer")
    elif end < start:
        raise ValueError("Ending number cannot be less than starting number")
    lst = []
    for _ in range(start, end + 1):
        lst.append(num ** _)
    return lst


def polygon_area(length, sides):
    """
    Returns area of a regular polygon between sides 3 and 6
    :param length: length of a side of a regular polygon
    :param sides: number of sides - supported between 3 and 6
    :return: Area of regular polygon. Precision is default float
    """
    if 0 < sides < 3:
        raise ValueError("Polygon needs to have a minimum of 3 sides")
    elif sides < 0:
        raise ValueError("Polygon cannot have negative sides")
    elif sides > 6:
        raise ValueError("This program only supports polgyon until 6 sides")
    elif length < 0:
        raise ValueError("Length of a side cannot be negative ")
    else:
        area = sides * (length ** 2) / (4 * tan(pi / sides))
    return area


def temp_converter(temp_f, temp_given_in):
    """
    Converts temperature from fahrenheit to celsius
    :param temp_f: temperature in fahrenheit
    :param temp_given_in: the UOM - only supported is 'f'
    :return: returns a temperature in Celsius. Precision is default float
    """

    if temp_given_in != 'f':
        raise ValueError('This program only handles conversion from fahrenheit represented as 'f' ')
    elif temp_f < -459.67:
        raise ValueError('The value entered is less than absolute zero')
    return (5 * (temp_f - 32)) / 9


# km/m/ft/yrd, time can be ms/s/m/hr/day
def speed_converter(speed_in_kmph, dist, time):
    """
    Takes speed in kmph and converts to a pre-defined list of UOMs
    :param speed_in_kmph: speed in kilometers per hour
    :param dist: predefined list of distance UOMs - km/m/ft/yrd
    :param time: predefined list of distance UOMs - ms/s/m/hr/day
    :return: returns a converted speed in the predefined list of conversions. Precision is default float
    """

    if dist not in ['km', 'm', 'ft', 'yrd']:
        raise ValueError("Distance UOM is incorrect")
    elif time not in ['ms', 's', 'm', 'hr', 'day']:
        raise ValueError("Time UOM is incorrect")
    elif speed_in_kmph < 0:
        raise ValueError("Speed cannot be negative")

    dict_dist = {'km_km': 1, 'km_m': 1000, 'km_ft': 3280.84, 'km_yrd': 1093.61}
    dict_time = {'hr_hr': 1, 'hr_s': 3600, 'hr_m': 60, 'hr_day': 0.0416, 'hr_ms': 36e5}

    if 'km' + '_' + dist not in dict_dist or 'hr' + '_' + time not in dict_time:
        raise KeyError("Key not found")
    else:
        return speed_in_kmph * dict_dist['km' + '_' + dist] / dict_time['hr' + '_' + time]


# time_it('print', 1, 2, 3, sep='-', repetitions=4)
#
# time_it('polygon_area', 15, sides=3)
#
# time_it('squared_power_list', 5, start=2, end=8,
#         repetitions=15)
#
# time_it('speed_converter', 200, dist='yrd', time='m',
#         repetitions=15)
#
# time_it('temp_converter', 200, temp_given_in='f',
#         repetitions=15)
