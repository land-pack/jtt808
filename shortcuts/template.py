"""
This class expect two argument,one is a request (a dicts type)
the another is a template split by a "|" string
"""
import sys

sys.path.append("..")
from utils.check_code import check


def render(request, ruler):
    """

    :param ruler:
    :type request: object
    """
    temp = []
    each = ruler.split("|")
    each.append('crc')  # Auto loader the old CRC for value
    for item in each:
        if item in request:
            if request[item]:
                for k in request[item]:
                    temp.append(k)
    check_code = check(temp)
    temp[-1] = check_code  # change to a new CRC
    temp.insert(0, 126)  # Add the header tag
    temp.append(126)  # Append the tail tag
    return tuple(temp)  # will got a tuple for response ...


def render_to_tuple(request):
    pass


if __name__ == '__main__':
    sample = {'abc': (1, 2), 'def': (3, 5), 'crc': (2,)}
    template = 'abc|def'
    result = render(sample, template)
    print result
