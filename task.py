# Function 1 Specification
# This function must have the following header: def conv_num(num_str). This function takes in a string and converts it into a base 10 number and returns it. It has the following specifications:

# Must be able to handle strings that represent integers
# Must be able to handle strings that represent floating point numbers
# Must be able handle hexadecimal numbers with the prefix 0x
# Must be case insensitive
# Negative numbers are indicated with a - like -0xFF
# The type returned must match the type sent. For example, if an string of an integer is passed in, conv_num must return an int.
# Invalid formats should return None, including, but not limited to:
# strings with multiple decimal points
# strings with alpha that aren't part of a hexadecimal number
# strings with a hexadecimal number without the proceeding 0x
# values for num_str that are not strings or are empty strings
def conv_num(num_str):
    return

# Function 2 Specification
# This function must have the following header: def my_datetime(num_sec). This function takes in an integer value that represents the number of seconds since the epoch: January 1st 1970. The function takes num_sec and converts it to a date and returns it as a string with the following format: MM-DD-YYYY. It has the following specifications:

# It may be assumed that num_sec will always be an int value
# It may be assumed that num_sec will always be a non-negative value
# Must be able to handle leap years


def my_datetime(num_sec):
    return
# Function 3 Specification
# This function must have the following header: def conv_endian(num, endian='big'). This function takes in an integer value as num and converts it to a hexadecimal number. The endian type is determined by the flag endian. The function will return the converted number as a string. It has the following specifications:

# It may be assumed that num will always be an integer
# Must be able to handle negative values for num
# A value of big for endian will return a hexadecimal number that is big-endian
# A value of little for endian will return a hexadecimal number that is little-endian
# Any other values of endian will return None
# The returned string will have each byte separated by a space
# Each byte must be two characters in length


def conv_endian(num, endian='big'):
    return
