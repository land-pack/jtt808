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


def to_2_tuple(val):
    temp_list = []
    for item in val:
        temp = item.split('/')
        temp_tuple = tuple(temp)
        temp_list.append(temp_tuple)
    return temp_list


def get_argument(val):
    """
    :param val: 'val)'
    :return: 'val'
    """
    item = val.split(')')
    return str(item[0])


# Example function !
def is_okay():
    return True


def is_bad(val):
    """
    You maybe want to check some field before get the range of field !
    :param val:
    :return:
    """
    print 'val is ', val
    return False


sample_function_dict = {'is_okay': is_okay,
                        'is_bad': is_bad
                        }

if __name__ == '__main__':
    # example1 = pattern(
    #         ('abc', '123'),
    #         ('def', '456')
    # )
    # print example1

    # Just like a new template language!
    example2 = ['flag/9', 'dev_id/is_bad(flag)?3~3:2~5', 'tie/3', 'ghi/4', 'time/4']
    empty_dict = {'flag': 9}
    for index in range(len(example2)):
        # empty_dict = {}
        print multi_optional(empty_dict, example2[index], sample_function_dict)

        # to_fixed_dict(example2)
