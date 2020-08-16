import pytest
import random
import string
import session5
import os
import inspect
import re
import math

README_CONTENT_CHECK_FOR = [
    'time_it',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter',
]

CHECK_FOR_THINGS_NOT_ALLOWED = [
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme_words = [word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 50, "Make your README.md file interesting! Add atleast 50 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 4


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_time_it_repetitions_type():
    with pytest.raises(TypeError) as e_info:
        r = session5.time_it('print', 1, 2, 3, repetitions='a')


def test_time_it_repetitions_count():
    with pytest.raises(ValueError) as e_info:
        r = session5.time_it('print', 1, 2, 3, repetitions=-1)


def test_time_it_invalid_function():
    with pytest.raises(ValueError) as e_info:
        r = session5.time_it('type', 1, 2, 3, repetitions=5)


def test_time_it_no_args():
    with pytest.raises(TypeError) as e_info:
        r = session5.time_it()


def test_squared_power_list_non_int_input():
    with pytest.raises(TypeError) as e_info:
        r = session5.squared_power_list('a', 2, 5)


def test_squared_power_list_ending_smaller():
    with pytest.raises(ValueError):
        r = session5.squared_power_list(3, 5, 2)


def test_squared_power_list():
    assert session5.squared_power_list(3, 1, 3) == [3, 9, 27], "squared power list is not working!"


def test_polygon_area_negative_length():
    with pytest.raises(ValueError) as e_info:
        r = session5.polygon_area(-1, 3)


def test_polygon_area_negative_side():
    with pytest.raises(ValueError) as e_info:
        r = session5.polygon_area(1, -3)


def test_polygon_area_less_than_two_sides():
    with pytest.raises(ValueError) as e_info:
        r = session5.polygon_area(1, 1)


def test_polygon_area_greater_than_six_sides():
    with pytest.raises(ValueError) as e_info:
        r = session5.polygon_area(1, 8)


def test_polygon_area_square():
    assert math.isclose(session5.polygon_area(3, 4), 9), "Area of square is not matching"


def test_temp_converter_not_fahrenheit():
    with pytest.raises(ValueError) as e_info:
        r = session5.temp_converter(100, 'c')


def test_temp_converter_subzero_kelvin():
    with pytest.raises(ValueError) as e_info:
        r = session5.temp_converter(-500, 'f')


def test_temp_converter():
    assert math.isclose(session5.temp_converter(212, 'f'), 100), "The temperature conversion is incorrect"


def test_speed_converter_incorrect_dist_uom():
    with pytest.raises(ValueError) as e_info:
        r = session5.speed_converter(200, 'in', 's')


def test_speed_converter_incorrect_time_uom():
    with pytest.raises(ValueError) as e_info:
        r = session5.speed_converter(200, 'km', 'microsec')


def test_speed_converter_negative_speed():
    with pytest.raises(ValueError) as e_info:
        r = session5.speed_converter(-10, 'km', 'hr')


def test_speed_converter():
    assert math.isclose(session5.speed_converter(60, 'km', 'm'), 1), "speed conversion is not working"

# def test_speed_converter():
#     with pytest.raises()
#
#
# def time_it_no_args():
