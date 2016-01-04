def pattern(*val):
    """
    To make a tuple being a Dicts!
    :param val: a tuple-inline a tuple from the apps-urls.py
    :return: a Dicts
    """
    temp = {}
    for item in val:
        temp[item[0]] = item[1]
    return temp


if __name__ == '__main__':
    example = pattern(
            ('abc', '123'),
            ('def', '456')
    )
    print example
