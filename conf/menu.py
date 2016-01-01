"""
TODO something ...
"""
from core.urls import pattern

"""
This is a Request - Response Dicts
Why need those middle ware?
because, sometime we have many-to-many relationship!
ser     : server
ter     : terminal
req     : request
rsp     : response
reg     : register
aut     : authentication
loc     : location
com     : commonly
"""

REQ_RSP = pattern(
        ('ter_reg_req', 'ser_reg_rsp'),
        ('ter_aut_req', 'ser_com_rsp')
)

if __name__ == '__main__':
    for req in REQ_RSP:
        print 'Request is :%s -- Response is :%s' % (req, REQ_RSP[req])
