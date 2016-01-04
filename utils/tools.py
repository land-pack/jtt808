"""
some tool work for batter
Like example (1,2) become 0000 0001 0000 0010
and the digist should be :512+2=514
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

if __name__ == '__main__':
    sample1 = (127, 2)
    print is_subpackage(sample1)
    sample2 = (1023, 0)
    print is_encryption(sample2)
