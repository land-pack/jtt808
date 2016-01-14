"""
some tool work for batter
Like example (1,2) become 0000 0001 0000 0010
and the digit should be :512+2=514
"""
from utils.check_code import check


def is_subpackage(val):
    """

    :param val: a tuple
    :return: a decimal digit!
    """
    temp = val[0]
    if temp & 64:
        return True
    else:
        return False


def is_encryption(val):
    """
    checking the 10bit if it's fill '1' mean use RSA encrytion
    return True else return False
    :return: BOOL
    """
    temp = val[0]
    if temp & 1024:
        return True  # RSA encryption!
    else:
        return False


def is_complete(val, std):
    """
    if the client crc equal the calculate value
    and then return True else return False!
    :param val:
    :return:
    """
    result = check(val)
    if result == std:
        return True  # The crc encryption equal the client send!
    else:
        return False


def field_langth(val):
    """
    Sometime,we don't know each field length before we resolute it!
    So,we need to calculate some field and then get the exactly length!
    That's why we need this function!
    :param val:
    :return: Integer value
    """
    return int(val[0])


def dec2hex4tuple(val):
    """
    :rtype: object
    :param val: a tuple ,which include decimal number!
    :return: a tuple ,which include hex number!
    """
    temp = []
    for item in val:
        temp_item = hex(item).replace('0x', '')
        temp_save = int(temp_item)
        temp.append(temp_save)
    return tuple(temp)


def to_dword(val):
    """
    :param val: a tuple (2, 110, 226, 147)
    :return:40821395 but what we need is range(38.0000 ~ 42.00000)
    """
    temp_hex = []
    for item in val:
        temp_hex.append(hex(item))
    temp_str = ''
    for item in temp_hex:
        temp_str += str(item).replace('0x', '')
    result = int(temp_str, 16)
    return result


def to_double_word_fun(val):
    """
    :param val: a tuple (2, 110, 226, 147)
    :return: (38.0000 ~ 42.00000)
    """
    a_value = to_dword(val)
    temp = float(a_value)
    ret = temp / 1000000
    return ret


def to_int_dword_fun(val):
    a_value = to_dword(val)
    temp = int(a_value)
    return temp


def to_a_word_fun(val):
    """
    :param val: a tuple with two element (2, 110)
    :return:
    """
    a_value = to_dword(val)
    temp = float(a_value)
    return temp


if __name__ == '__main__':
    sample1 = (127, 2)
    print is_subpackage(sample1)
    sample2 = (1023, 0)
    print is_encryption(sample2)

    print '----------Test to_dword --------------'
    sample5 = (2, 110, 226, 147)
    sample5x = to_dword(sample5)
    print 'old      :', sample5
    print 'new      :', sample5x

    print '---------Test to_position-----------'
    sample6 = (6, 168, 93, 143)
    print 'old      :', sample6
    print 'new      :', to_double_word_fun(sample6)

    print '---------Test to_altitude----------'
    sample7 = (4, 89)
    print 'old      :', sample7
    print 'new      :', to_a_word_fun(sample7)

    print '---------Test to_int_dword---------'
    sample8 = (6, 168)
    print 'old      :', sample8
    print 'new      :', to_int_dword_fun(sample8)
