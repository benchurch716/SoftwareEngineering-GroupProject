import string
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
# 
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
def _validate_int(num_str, isPositive):
    if isPositive:
        if num_str.isdigit():
            return True
    else:
        # check all but the '-'
        if (num_str[1:].isdigit()):
            return True
    return False


def _convert_int(num_str, isPositive):
    return "i'm an int"


def _validate_float(num_str, isPositive):
    # check for more than 1 decimal places
    decimal_counter = 0
    for char in num_str:
        if char == ".":
            decimal_counter += 1
    if (decimal_counter > 1):
        return False
    elif(decimal_counter == 1):
        # Check for non digits
        if isPositive:
            num_str = num_str.replace('.','')
            if(num_str.isdigit):
                return True
            else:
                return False
        else:
            num_str = num_str.replace('.','')
            # check all but the '-'
            if (num_str[1:].isdigit()):
                return True
            else:
                return False
    else:
        return False

def _convert_float(num_str, isPositive):
    return "i'm a float"

def _validate_hex(num_str, isPositive):
    if "0x" in num_str:
        # check for non hex letters after the "0x"
        if isPositive:
            if all(char in string.hexdigits for char in num_str[2:]):
                return True
            else: 
                return False
        else:
            # check all but the '-0x'
            if all(char in string.hexdigits for char in num_str[3:]):
                return True
            else:
                return False
    return False

def _convert_hex(num_str, isPositive):
    return "i'm a hex"

def conv_num(num_str):
    # check for not a string
    if type(num_str) is not str:
        return None
    # check for empty string
    if (len(num_str) == 0):
        return None
    # check for negative
    isPositive = True
    if (num_str.startswith('-')):
        isPositive = False
    # check int
    if(_validate_int(num_str, isPositive)):
        return _convert_int(num_str, isPositive)
    # check for Float
    if(_validate_float(num_str, isPositive)):
        return _convert_float(num_str, isPositive)
    # check for Hex
    if(_validate_hex(num_str, isPositive)):
        return _convert_hex(num_str, isPositive)
    return None


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
    return
