def dec2hex4string(val):
    """
    :param val: a tuple ,which include decimal number!
    :return: a tuple ,which include hex number!
    """
    temp = []
    for item in val:
        temp_item = hex(item).replace('0x', '')
        temp.append(temp_item)

    result = ''.join(temp)
    return result


def dec2hex(val):
    temp = dec2hex4string(val)
    return int(temp, 16)


def convert_to_byte(val):
    pass


def convert_to_word(val):
    pass


def convert_to_dword(val):
    pass


def convert_to_byte_n(val):
    pass


def convert_to_bcd_n(val):
    pass


def convert_to_string(val):
    pass


if __name__ == '__main__':
    print '---------------Test dec2hex4string function ----------------'
    sample1 = [126, 128, 22, 1, 0, 126]
    result1 = dec2hex4string(sample1)
    print 'sample1      :', sample1
    print 'result1      :', result1

    print '---------------Test dec2hex function ----------------'
    sample2 = [2, 110, 95, 32]
    result2 = dec2hex(sample2)
    print 'sample1      :', sample2
    print 'result1      :', result2
