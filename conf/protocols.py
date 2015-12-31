"""
0x
"""
from core.urls import pattern
from core.dns import dns
from core.dns import dns_key

JTT808 = pattern(
        ('register', 0x8100),
        ('unregister', 0x8200)
)
"""
ser     : server
ter     : terminal
req     : request
rsp     : response
reg     : register
aut     : authentication
loc     : location
com     : commonly
"""
MSG_ID_ORIGINAL = pattern(
        ('0x0100', 'ter_reg_req'),
        ('0x8100', 'ser_reg_rsp'),
        ('0x0102', 'ter_aut_req'),
        ('0x8001', 'ser_com_rsp')
)
"""
change the MSG_ID_ORIGINAL Dicts key
example: 0x0100 --> (1,0)
"""
MSG_ID = dns_key(MSG_ID_ORIGINAL)

if __name__ == '__main__':

    for item in MSG_ID:
        print 'Request is   :%s -- Response is  :%s' % (item,MSG_ID[item])


