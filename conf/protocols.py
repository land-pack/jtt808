"""
0x8100 Poor readability,so we need to give a name
to it.how about 'ter_reg_req' as it nickname!
"""
from core.urls import pattern
from core.dns import dns_key, dns_k2v
from utils.authentication import simple_auth

AUTH_CODE = simple_auth()
SYSTEM_CMD = pattern(
        ('sys_ok', (0,)),
        ('sys_err', (2, 0)),
        ('sys_crc', (1,)),
        ('sys_auth', AUTH_CODE),
        ('sys_product', (0, 1)),
        ('sys_fixed_msg_attr', (0, 5))  # This is a fixed value ,you should calculate the msg attr yourself!
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
get     : get
info    : information
"""
MSG_ID_ORIGINAL = pattern(
        ('0x0100', 'ter_reg_req'),
        ('0x8100', 'ser_reg_rsp'),
        ('0x0102', 'ter_aut_req'),
        ('0x8001', 'ser_com_rsp'),
        ('0x0200', 'position'),
        ('0x8104', 'get_ter_info'),
        ('0x0104', 'get_ter_info_rsp')
)

"""
change the MSG_ID_ORIGINAL Dicts key
example1: 0x0100 --> (1,0)
example2: 0100 --> (1,2)
"""
MSG_ID = dns_key(MSG_ID_ORIGINAL)
SYS_ID = dns_k2v(MSG_ID)

if __name__ == '__main__':
    print 'MSG_ID       :', MSG_ID
    print 'SYSTEM_CMD   :', SYSTEM_CMD
    print 'SYS_ID       :', SYS_ID
