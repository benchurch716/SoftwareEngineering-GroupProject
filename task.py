import string
# Function 1 Specification - BEN
# This function must have the following header: def conv_num(num_str).
# This function takes in a string and converts it into a base 10 number
# and returns it.
# It has the following specifications:

# Must be able to handle strings that represent integers
# Must be able to handle strings that represent floating point numbers
# Must be able handle hexadecimal numbers with the prefix 0x
# Must be case insensitive
# Negative numbers are indicated with a - like -0xFF
# The type returned must match the type sent.
# For example, if an string of an integer is passed in, conv_num
# must return an int.
# Invalid formats should return None, including, but not limited to:
# strings with multiple decimal points
# strings with alpha that aren't part of a hexadecimal number
# strings with a hexadecimal number without the proceeding 0x
# values for num_str that are not strings or are empty strings

# This function checks if the passed value is a valid integer for conv_num
# receives: num_str - The string to be converted
#            isPositive - true if the string doesn't start with a "-"
# returns: True - If the input only contains numbers
#          False - If the data is invalid


def _map_char_value(digit):
    values = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
              'F': 15}
    return values[digit.upper()]


def _validate_int(num_str):
    return num_str.isdigit()


def _convert_int(num_str, isPositive):
    result = 0
    # loop through string and convert the string to unicode,
    places_count = len(num_str)
    for digit in num_str:
        result += _map_char_value(digit) * (10 ** (places_count-1))
        places_count = places_count - 1
    if isPositive:
        return result
    else:
        return result * -1


def _validate_float(num_str):
    # check for more than 1 decimal places
    decimal_counter = 0
    for char in num_str:
        if char == ".":
            decimal_counter += 1
    if (decimal_counter > 1):
        return False
    elif(decimal_counter == 1):
        # remove decimal point
        num_str = num_str.replace('.', '')
        # Check for non digits
        if(num_str.isdigit()):
            return True
        else:
            return False
    else:
        return False


def _convert_float(num_str, isPositive):
    # break string into the int and fractional components
    decimal_index = num_str.find('.')
    int_componet = num_str[0:decimal_index]
    fraction_componet = num_str[decimal_index + 1:]
    # convert the int component
    result = _convert_int(int_componet, True)
    # convert the decimal componet
    places_count = -1
    for digit in fraction_componet:
        result += _map_char_value(digit) * (10 ** places_count)
        places_count = places_count - 1
    # return the result
    if isPositive:
        return result
    else:
        return result * -1


def _validate_hex(num_str):
    if "0x" in num_str:
        # check for non hex letters after the "0x"
        if all(char in string.hexdigits for char in num_str[2:]):
            return True
        else:
            return False
    return False


def _convert_hex(num_str, isPositive):
    result = 0
    # remove "0x" prefix
    num_str = num_str[2:]
    # loop through string and convert each digit
    places_count = len(num_str)
    for digit in num_str:
        result += _map_char_value(digit) * (16 ** (places_count-1))
        places_count = places_count - 1
    # return result
    if isPositive:
        return result
    else:
        return result * -1


def conv_num(num_str):
    # check for not a string
    if type(num_str) is not str:
        return None
    # check for empty string
    if (len(num_str) == 0):
        return None
    # check for negative and remove "-"
    isPositive = True
    if (num_str.startswith('-')):
        isPositive = False
        num_str = num_str[1:]
    # check for int
    if(_validate_int(num_str)):
        return _convert_int(num_str, isPositive)
    # check for Float
    if(_validate_float(num_str)):
        return _convert_float(num_str, isPositive)
    # check for Hex
    if(_validate_hex(num_str)):
        return _convert_hex(num_str, isPositive)
    return None


# Function 2 Specification - TROY
# This function must have the following header: def my_datetime(num_sec).
# This function takes in an integer value that represents the number of
# seconds since the epoch: January 1st 1970.
# The function takes num_sec and converts it to a date and returns it as a
# string with the following format: MM-DD-YYYY.

# It has the following specifications:
# It may be assumed that num_sec will always be an int value
# It may be assumed that num_sec will always be a non-negative value
# Must be able to handle leap years


def my_datetime(num_sec):

    months = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    month, day, year = 1, 1, 1970
    SECONDS_IN_DAY = 86400
    SECONDS_IN_YEAR = SECONDS_IN_DAY*365
    SECONDS_IN_LEAP_YEAR = SECONDS_IN_DAY * 366

    while num_sec > SECONDS_IN_YEAR:
        num_sec -= SECONDS_IN_YEAR
        year += 1
        if year >= 1972 and leap_check(year):
            SECONDS_IN_YEAR = SECONDS_IN_LEAP_YEAR
        else:
            SECONDS_IN_YEAR = SECONDS_IN_DAY*365

    while num_sec > months[month] * SECONDS_IN_DAY:
        num_sec -= months[month] * SECONDS_IN_DAY
        months[2] = 28
        month += 1
        if month == 2 and leap_check(year):
            months[month] = 29

    while num_sec > 0:
        if month == 2 and leap_check(year):
            months[month] = 29
        last = num_sec//SECONDS_IN_DAY
        num_sec = 0
        if last < months[month]:
            day += last
        else:
            day = months[month]

    if month < 10:
        month = '0' + str(month)

    if day < 10:
        day = '0' + str(day)

    return str(month) + '-' + str(day) + '-' + str(year)


def leap_check(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif (year - 1972) % 4 == 0:
        return True


# Function 3 Specification - PAUL
# This function must have the following header:
# def conv_endian(num, endian='big').
# This function takes in an integer value as num and converts it to a
# hexadecimal number.
# The endian type is determined by the flag endian.
# The function will return the converted number as a string. It has the
# following specifications:

# It may be assumed that num will always be an integer
# Must be able to handle negative values for num
# A value of big for endian will return a hexadecimal number that is big-endian
# A value of little for endian will return a hexadecimal number that is
# little-endian
# Any other values of endian will return None
# The returned string will have each byte separated by a space
# Each byte must be two characters in length


def conv_endian(num, endian='big'):
    MAX_HEX_VALUE = 15
    if endian != 'big' and endian != 'little':
        return None
    bt_vals = []
    bt_str = ''

    if num >= 0:
        hex_str = ''
    else:
        hex_str = '-'
        num = abs(num)

    hex_map = [
        '0', '1', '2', '3', '4', '5', '6', '7',
        '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    # extract hex values from num and store in a list of bytes
    while num > MAX_HEX_VALUE:
        rem = num % 16  # get remainder to map to hex
        num = num // 16
        hex = hex_map[rem]
        bt_str = hex + bt_str
        if len(bt_str) == 2:
            bt_vals.insert(0, bt_str)
            bt_str = ''

    bt_str = hex_map[num] + bt_str  # add remaining hex value to string

    # add 0 padding to a byte with one character
    if len(bt_str) == 1:
        bt_str = '0' + bt_str

    bt_vals.insert(0, bt_str)  # add final byte to byte list

    if endian == 'big':
        dir = 1
    else:
        dir = -1

    for bt in bt_vals[::dir]:
        hex_str = hex_str + bt + ' '

    # return the string without the last character to drop the trailing space
    return hex_str[:-1]
