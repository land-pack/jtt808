"""
According the message id,this function will dispatch each to
it destination!
"""
from utils.tools import is_subpackage
from utils.tools import is_encryption
from utils.tools import is_complete
from conf.protocols import JTT808


class Split:
    """
    This class expect a tuple,something like
    (126,1,0,1,2,1) and the class will split it
    to {'tag':126,'msg_id':(1,0),'msg_attr':(1,2)}
    """

    def __init__(self, val):

        self.message_head_content = val[1:-2]
        self.crc = val[-2]  # The crc encryption from terminal!
        self.debug = True
        if is_complete(self.message_head_content, self.crc):
            self.tag = val[0:1]
            self.msg_id = val[1:3]
            self.msg_attr = val[3:5]
            self.dev_id = val[5:11]
            self.msg_product = val[11:13]
            self.end_tag = val[-1:]
            # check if subpackage
            if is_subpackage(self.msg_attr):
                self.package_item = val[13:15]
                self.content = val[15:-2]
            else:
                # No message package item optional
                self.content = val[13:-2]
                # check if use CRC (Cyclic Redundancy Check)
                if is_encryption(self.msg_attr):
                    # TODO something for deciphering
                    pass
        else:
            # ignore this request from terminal device
            self.debug = False

    def show(self):
        if self.debug:
            print 'self.tag         :', self.tag
            print 'self.msg_id      :', self.msg_id
            print 'self.msg_attr    :', self.msg_attr
            print 'self.dev_id      :', self.dev_id
            print 'self.content     :', self.content
            print 'self.crc         :', self.crc
            print 'self.end_tag     :', self.end_tag
        else:
            print 'There are no assign because the crc have no right!'


class Dispatch:
    """
    According the JTT808 protocol, and what we should do
    depend on message id! so, if you want to know what current
    message id mean! you should ask the protocol!
    """

    def __init__(self, protocol=JTT808):
        self.protocol = protocol

    def distribute(self, msg_id):
        """

        :param msg_id: is a Dicts and system will ask if exists!
        :return:
        """
        if msg_id in self.protocol:
            pass

if __name__ == '__main__':
    sample = (126, 1, 0, 0, 2, 78, 56, 45, 34, 25, 78, 0, 1, 51, 52, 43, 126)
    result = Split(sample)
    result.show()
