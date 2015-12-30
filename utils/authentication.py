from datetime import datetime


def simple():
    """
    :return: just a string like 20151230
    """
    return str(datetime.today().date()).replace('-', '')
