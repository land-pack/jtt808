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
    if '~' in item[1]:
        range_to = item[1].split('~')
        result[item[0]] = [int(x) for x in range_to]  # Very nice code
    else:
        result[item[0]] = int(item[1])
    return result


def to_fixed_dict_super(val):
    item = val.split('/')
    result = {}
    range_value = item[1]
    range_key = item[0]

    if '?' in range_value:
        condition = range_value.split('?')
        print 'condition    :', condition
    else:
        if '~' in range_value:
            range_to = range_value.split('~')
            result[range_key] = [int(x) for x in range_to]  # Very nice code
        else:
            result[range_key] = int(range_value)
    return result


def multi_optional(val, func_dict):
    if '/' in val:
        field_name = val.split('/')
        result = {}
        range_value = field_name[1]
        range_key = field_name[0]
        if '?' in range_value:
            func_range_value = range_value.split('?')
            func_name = func_range_value[0]
            optional_range = func_range_value[1]
            if ':' in optional_range:
                optional_tuple = optional_range.split(':')
                optional_a = optional_tuple[0]
                optional_b = optional_tuple[1]
                if func_name in func_dict:  # Looking for the checking function in the Dicts!
                    condition_function = func_dict[func_name]
                    if condition_function():  # It's return True
                        optional_finally = optional_a
                    else:
                        optional_finally = optional_b
                    if '~' in optional_finally:
                        print 'optional_finally', optional_finally
                        range_to = optional_finally.split('~')
                        result[range_key] = [int(x) for x in range_to]  # Very nice code
                    else:
                        result[range_key] = int(optional_finally)
        else:
            if '~' in range_value:
                range_to = range_value.split('~')
                result[range_key] = [int(x) for x in range_to]  # A tuple! Very nice code
            else:
                result[range_key] = int(range_value)  # Only a Integer value!

    else:
        print "Your field define are no right syntax! ('dev_id/2')"

    return result


# Example function !
def is_okay():
    return True


def is_bad():
    return False


sample_function_dict = {'is_okay': is_okay,
                        'is_bad': is_bad
                        }

if __name__ == '__main__':
    example1 = pattern(
            ('abc', '123'),
            ('def', '456')
    )
    print example1

    # Just like a new template language!
    example2 = ['dev_id/is_bad?3~3:2~5', 'tie/3', 'ghi/4', 'time/4']
    for index in range(len(example2)):
        print multi_optional(example2[index], sample_function_dict)

        # to_fixed_dict(example2)
