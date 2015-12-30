"""
According the message id,this function will dispatch each to
it destination!
"""
from utils.tools import is_subpackage
from utils.tools import is_encryption


class Split:
    """
    This class expect a tuple,something like
    (126,1,0,1,2,1) and the class will split it
    to {'tag':126,'msg_id':(1,0),'msg_attr':(1,2)}
    """

    def __init__(self, val):
        self.tag = val[0:1]
        self.msg_id = val[1:3]
        self.msg_attr = val[3:5]
        self.dev_id = val[5:11]
        self.msg_product = val[11:13]
        if is_subpackage(self.msg_attr):
            self.package_item = val[13:15]
            self.content = val[15:-2]
        else:
            # No message package item optional
            self.content = val[13:-2]
        self.crc = val[-2:-1]
        self.end_tag = val[-1:]

    def show(self):
        print 'self.tag         :', self.tag
        print 'self.msg_id      :', self.msg_id
        print 'self.msg_attr    :', self.msg_attr
        print 'self.dev_id      :', self.dev_id
        print 'self.content     :', self.content
        print 'self.crc         :', self.crc
        print 'self.end_tag     :', self.end_tag


if __name__ == '__main__':
    sample = (126, 1, 0, 0, 2, 78, 56, 45, 34, 25, 78, 0, 1, 51, 52, 185, 126)
    result = Split(sample)
    result.show()
