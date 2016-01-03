"""
This class expect two argument,one is a request (a dicts type)
the another is a template split by a "|" string
"""
import sys
sys.path.append("..")
from utils.check_code import check
from conf.protocols import SYSTEM_CMD


def render(request, ruler):
    """

    :param ruler:
    :type request: object
    """
    system_cmd = SYSTEM_CMD
    temp = []
    each = ruler.split("|")
    each.append('crc')  # Auto loader the old CRC for value
    for item in each:  # loader the data format by ruler
        if item in request:  # if the key in the request ,and go get it!
            if type(request[item]) is tuple:  # because ,the value belong to The request Dicts, also the value is tuple!
                for k in request[item]:  # get each element of the tuple!
                    temp.append(k)
        elif item in system_cmd:
            if type(system_cmd[item]) is tuple:
                for k in system_cmd[item]:
                    temp.append(k)

    check_code = check(temp)
    temp[-1] = check_code  # change to a new CRC
    temp.insert(0, 126)  # Add the header tag
    temp.append(126)  # Append the tail tag
    return tuple(temp)  # will got a tuple for response ...


if __name__ == '__main__':
    sample = {'abc': (1, 2), 'def': (3, 5), 'crc': (2,)}
    template = 'abc|def'
    result = render(sample, template)
    print result