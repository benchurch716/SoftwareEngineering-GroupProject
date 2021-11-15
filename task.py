# Function 1 Specification - BEN
# This function must have the following header: def conv_num(num_str).
# This function takes in a string and converts it into a base 10 number and returns it. It has the following specifications:

# Must be able to handle strings that represent integers
# Must be able to handle strings that represent floating point numbers
# Must be able handle hexadecimal numbers with the prefix 0x
# Must be case insensitive
# Negative numbers are indicated with a - like -0xFF
# The type returned must match the type sent.
# For example, if an string of an integer is passed in, conv_num must return an int.
# Invalid formats should return None, including, but not limited to:
# strings with multiple decimal points
# strings with alpha that aren't part of a hexadecimal number
# strings with a hexadecimal number without the proceeding 0x
# values for num_str that are not strings or are empty strings
def conv_num(num_str):
    return


# Function 2 Specification - TROY
# This function must have the following header: def my_datetime(num_sec).
# This function takes in an integer value that represents the number of seconds since the epoch: January 1st 1970.
# The function takes num_sec and converts it to a date and returns it as a string with the following format: MM-DD-YYYY.

# It has the following specifications:
# It may be assumed that num_sec will always be an int value
# It may be assumed that num_sec will always be a non-negative value
# Must be able to handle leap years


def my_datetime(num_sec):
    return


# Function 3 Specification - PAUL
# This function must have the following header: def conv_endian(num, endian='big').
# This function takes in an integer value as num and converts it to a hexadecimal number.
# The endian type is determined by the flag endian.
# The function will return the converted number as a string. It has the following specifications:

# It may be assumed that num will always be an integer
# Must be able to handle negative values for num
# A value of big for endian will return a hexadecimal number that is big-endian
# A value of little for endian will return a hexadecimal number that is little-endian
# Any other values of endian will return None
# The returned string will have each byte separated by a space
# Each byte must be two characters in length


def conv_endian(num, endian='big'):
    hex_vals = []
    bt_str = ''
    hex_str = ''
    hex_map = [
        '0', '1', '2', '3', '4', '5', '6', '7',
        '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    # extract hex values from num and store in a list of bytes
    while num > 15:
        rem = num % 16  # get remainder to map to hex
        num = num // 16
        hex = hex_map[rem]
        bt_str = hex + bt_str
        if len(bt_str) == 2:
            hex_vals.insert(0, bt_str)
            bt_str = ''

    bt_str = hex_map[num] + bt_str  # add remaining hex value to string

    # add 0 padding to a byte with one character
    if len(bt_str) == 1:
        bt_str = '0' + bt_str

    hex_vals.insert(0, bt_str)  # add final byte to byte list

    if endian == 'big':
        dir = -1
    else:
        dir = 1

    for bt in hex_vals[::dir]:
        hex_str = hex_str + bt + ' '

    # return the string without the last character to drop the trailing space
    return hex_str[:-1]


if __name__ == '__main__':
    result = conv_endian(954786)
    print(result)
    print(len(result))
    print(conv_endian(954786, 'little'))
    print(conv_endian(10742015))
