"""
some tool work for batter
Like example (1,2) become 0000 0001 0000 0010
and the digist should be :512+2=514
"""
from utils.check_code import check
import time


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


def to_bcd(val):
    """
    :param val: a tuple ,which include decimal number!
    :return: a tuple ,which include hex number!
    """
    temp = []
    for item in val:
        temp_item = hex(item).replace('0x', '')
        temp_save = int(temp_item)
        temp.append(temp_save)

    return tuple(temp)


def to_datetime(val):
    date = val[0:3]
    the_time = val[3:6]
    sub_date = '20'
    sub_time = ' '
    count = 0
    for item in date:
        sub_date += str(item)
        if count < 2:
            sub_date += '-'
        count += 1

    count = 0
    for item in the_time:
        sub_time += str(item)
        if count < 2:
            sub_time += ':'
        count += 1
    datetime = sub_date + sub_time
    return datetime


def to_sec(val):
    sec = time.mktime(time.strptime(val, '%Y-%m-%d %H:%M:%S'))
    temp = int(sec)
    return str(temp)


def to_timestamp(val):
    temp = to_datetime(val)
    return to_sec(temp)


if __name__ == '__main__':
    sample1 = (127, 2)
    print is_subpackage(sample1)
    sample2 = (1023, 0)
    print is_encryption(sample2)

    print '----------Test dec2hex----------------'
    sample3 = (22, 1, 5, 17, 64, 25)
    result3 = to_bcd(sample3)
    print 'old      :', sample3
    print 'new      :', result3
    #
    print '----------Test to_datetime------------'
    new_datetime = to_datetime(result3)
    print 'new      :', new_datetime

    print '----------Test to_sec ----------------'
    print 'the sec      :', to_sec(new_datetime)
