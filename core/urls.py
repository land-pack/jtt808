
def pattern(*val):
    """
    :param val: a tuple-inline a tuple from the apps-urls.py
    :return:
    """

    temp = {}
    for item in val:
        temp[item[0]] = item[1]

    return temp


def reflect(val):
    """
    :param val: a message id , and this function will try to response it!
    :return:
    """
    pass

if __name__ == '__main__':
    urlpatterns = pattern(
            ('register', 123),
            ('unregister', 456)

    )

    print urlpatterns
