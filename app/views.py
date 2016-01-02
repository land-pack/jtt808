from shortcuts.template import render



def register(request):
    """
    :param request: original data format to Dicts from terminal!
    :return: a render which a tuple factory
    you should know what you are doing and which field you need!
    """
    template = 'msg_id|msg_attr|dev_id|t_product|content'
    return render(request, template)


def auth(request):
    template = 'msg_id|msg_attr|dev_id|t_product|content'
    return render(request, template)


def server_commonly_response(request):
    template = 't_product|msg_id|msg_attr|sys_err|sys_err|sys_auth'
    return render(request, template)


def hello(request):
    print 'The request is -->  :', request


if __name__ == '__main__':
    """
    The below sample dicts just for test the register!
    """
    request = {'msg_id': (1, 2), 'msg_attr': (0, 2), 'dev_id': (153, 17, 152, 64, 130, 104), 't_product': (0, 1),
               'content': (81, 82), 'crc': (185,)}
    example = server_commonly_response(request)
    print 'example      :', example
