"""
0x8100 Poor readability,so we need to give a name
to it.how about 'ter_reg_req' as it nickname!
"""
from core.urls import pattern
from core.dns import dns_key
from utils.authentication import simple_auth

MSG_STRUCTURE = (
    'msg_id',
    'msg_attr',
    'dev_id',
    'content',
    'crc',
)

AUTH_CODE = simple_auth()
SYSTEM_CMD = pattern(
        ('sys_ok', (1, 0)),
        ('sys_err', (2, 0)),
        ('sys_auth', AUTH_CODE)
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
example1: 0x0100 --> (1,0)
example2: 0100 --> (1,2)
"""
MSG_ID = dns_key(MSG_ID_ORIGINAL)

if __name__ == '__main__':
    for item in MSG_ID:
        print 'Request is   :%s -- Response is  :%s' % (item, MSG_ID[item])

    for item in SYSTEM_CMD:
        print 'system_cmd is   %s   -- value is :%s' % (item,SYSTEM_CMD[item])