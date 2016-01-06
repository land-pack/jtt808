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


def to_fixed_dict(val):
    item = val.split('/')
    result = {}
    result[item[0]] = int(item[1])
    return result


if __name__ == '__main__':
    example1 = pattern(
            ('abc', '123'),
            ('def', '456')
    )
    print example1

    example2 = ['dev_id/2', 'tie/3', 'ghi/4', 'time/4']
    for index in range(len(example2)):
        print to_fixed_dict(example2[index])

        # to_fixed_dict(example2)
