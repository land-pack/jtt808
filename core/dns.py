import struct
import binascii
from ast import literal_eval
from utils.tools import dec2hex4tuple


def dns(val):
    """
    This function work for resolve the user conf to something system
    understand syntax ! example: '0x8100' -> '(128,1)'
    :param val:
    :return:
    """
    val = val.replace('0x', '')
    val = binascii.unhexlify(val)
    data_len = len(val)
    s = struct.Struct('%iB' % data_len)
    temp_dec_k = s.unpack(val)
    # temp_hex_k = dec2hex(temp_dec_k)
    return temp_dec_k


"""
Reset a Dict your give
and change it key example below:
'8100' --> (129,1)
"""


def dns_key(val):
    """
    :param val: a Dicts type
    :return: return a new Dict with new key like a (tuple)
    """
    temp = {}
    for item in val:
        key = str(dns(item))
        temp[key] = val[item]

    return temp


def dns_value(val):
    temp = {}
    for item in val:
        temp[item] = str(dns(val[item]))
    return temp


def dns_k2v(val):
    result = {}
    temp = {value: key for key, value in val.items()}
    for item in temp:
        result[item] = literal_eval(temp[item])
    return result


if __name__ == '__main__':
    print '-----------Test dns()------------------'
    sample1 = '0x8100'
    print 'old  :', sample1
    print 'new  :', dns(sample1)

    print '-----------Test dns_key()--------------'
    sample2 = {'8100': 'abc', '0x9100': 'def', '0x7100': 'hij'}
    print 'old  :', sample2
    print 'new  :', dns_key(sample2)

    print '-----------Test dns_value()------------'
    sample3 = {'abc': '0x9100', 'def': '0x8100', 'hij': '0x7100'}
    print 'old  :', sample3
    print 'new  :', dns_value(sample3)

    print '-----------Test dns_k2v()--------------'
    sample4 = {'(1,2)': 'abc', '(3,4)': 'def'}
    print 'sample3      :', sample4
    print 'new sample3  :', dns_k2v(sample4)
