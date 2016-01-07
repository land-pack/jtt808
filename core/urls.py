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


def get_argument(val):
    """
    :param val: 'val)'
    :return: 'val'
    """
    item = val.split(')')
    return str(item[0])


def multi_optional(result, val, func_dict, temp_dict={}):
    if '/' in val:
        field_name = val.split('/')
        # result = {}  # The finally Dicts we will fill out with the data & the name your get!
        range_value = field_name[1]  # the field range! Example# (1,2,3,4,5,6) Your get 0~3 and get (1,2,3)
        range_key = field_name[0]  # The field name your are going to use! Example# result['name']='Frank'
        if '?' in range_value:  # If you want to set a value with something condition,you should use '?' mark!
            func_range_value = range_value.split('?')  # you should get a data Example# ['is_okay(a)','1~2:3~4'
            func_name_temp = func_range_value[0]  # you will got a function name! Example# 'is_okay'
            if '(' in func_name_temp:
                func_with_arg = func_name_temp.split('(')
                func_name = func_with_arg[0]
                check_field = get_argument(func_with_arg[1])
            optional_range = func_range_value[1]  # Now,you should have both value for choose! '1~2:3~4'
            if ':' in optional_range:  # So, if you want to use each field under different condition,keep going!
                optional_tuple = optional_range.split(':')  # Split the both guys!
                optional_a = optional_tuple[0]  # optional one
                optional_b = optional_tuple[1]  # optional two
                if func_name in func_dict:  # Looking for the checking function in the Dicts!
                    condition_function = func_dict[func_name]  # Get function object
                    # if check_field in result:
                    #     check_field_value = result[check_field] # Get 2~3
                if condition_function(check_field_value):  # If it's return True after check 'check_field'
                    optional_finally = optional_a  # Do this
                else:  # Do another ...
                    optional_finally = optional_b
                if '~' in optional_finally:
                    range_to = optional_finally.split('~')
                    temp_dict[range_key] = [int(x) for x in range_to]  # Very nice code
                else:
                    temp_dict[range_key] = int(optional_finally)
        else:
            if '~' in range_value:
                range_to = range_value.split('~')
                temp_dict[range_key] = [int(x) for x in range_to]  # A tuple! Very nice code
            else:
                temp_dict[range_key] = int(range_value)  # Only a Integer value!

    else:
        print "Your field define are no right syntax! ('dev_id/2')"
    return_split_ruler = temp_dict
    temp_dict.clear()
    return return_split_ruler


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
