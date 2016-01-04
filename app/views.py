from shortcuts.template import render


def register(val):
    """
    :param val: original data format to Dicts from terminal!
    :return: a render which a tuple factory
    you should know what you are doing and which field you need!
    """
    template = 'msg_id|msg_attr|dev_id|t_product|content'
    return render(val, template)


def auth(val):
    template = 'msg_id|msg_attr|dev_id|t_product|content'
    return render(val, template)


def server_commonly_response(val):
    # message header = 'sys_msg_id|msg_attr|dev_id|s_product'
    """
    :param val:
    :return:
    """
    print 'output client request ....by views.py-->', val
    msg_content = 't_product|msg_id|sys_ok'
    template = 'ser_com_rsp|sys_fixed_msg_attr|dev_id|sys_product|' + msg_content
    return render(val, template)


def position(val):
    print 'The request if position -->', val


def hello(val):
    print 'The request is -->  :', val


if __name__ == '__main__':
    """
    The below sample dicts just for test the register!
    """
    request = {'msg_id': (1, 2), 'msg_attr': (0, 2), 'dev_id': (153, 17, 152, 64, 130, 104), 't_product': (0, 1),
               'content': (81, 82), 'crc': (185,)}
    example = server_commonly_response(request)
    print 'example      :', example
