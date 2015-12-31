import struct
import binascii


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


if __name__ == '__main__':
    x = {'8100': 'abc', '0x9100': '123'}
    print 'old  :', x
    print 'new  :', dns_key(x)
"""
Result:
old  : {'0x9100': '123', '8100': 'abc'}
new  : {'(145, 0)': '123', '(129, 0)': 'abc'}
"""
