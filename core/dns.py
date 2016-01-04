import struct
import binascii
from ast import literal_eval


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
    return s.unpack(val)


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
    sample1 = {'8100': 'abc', '0x9100': '123'}
    print 'old  :', sample1
    print 'new  :', dns_key(sample1)
    sample2 = {'sys_ok': '0x9100', 'sys_err': '0x8100', 'sys_su': '0x7100'}
    print 'old  :', sample2
    print 'new  :', dns_value(sample2)
    print 'old  :', dns_value(sample2)
    new_guy = dns_value(sample2)
    # -------------------------------------
    sample3 = {'(1,2)': 'ser_rsp', '(3,4)': 'ok'}
    print 'sample3      :', sample3
    print 'new sample3  :', dns_k2v(sample3)
