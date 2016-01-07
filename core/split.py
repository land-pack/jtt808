from utils.tools import is_subpackage
from utils.tools import is_encryption
from utils.tools import is_complete
import re


def is_okay(val):
    print 'output by is_okay:', val
    return False


def filer_wave_line(val):
    temp = val.split('~')
    result = [int(x) for x in temp]
    return result


def split_ruler(val):
    if '?' in val:  # If you split_list have something like this Example# 'tie/is_okay(dev_id)?1~2:2~4'
        pattern = re.compile(r'(?P<field>.*)/(?P<fun>.*)\((?P<arg>.*)\)\?(?P<optA>.*):(?P<optB>.*)')
    else:
        if ':' in val:  # If you split_list have something like this Example# 'tie/1~2:1~4'
            pattern = re.compile(r'(?P<field>.*)/(?P<optA>.*):(?P<optB>.*)')
        else:  # If you split_list have something like this Example# 'tie/1'
            pattern = re.compile(r'(?P<field>.*)/(?P<optA>.*)')
    m = pattern.match(val)
    result = m.groupdict()
    if 'optA' in result:
        if '~' in result['optA']:
            result['optA'] = filer_wave_line(result['optA'])
        else:
            result['optA'] = int(result['optA'])
    if 'optB' in result:
        if '~' in result['optB']:
            result['optB'] = filer_wave_line(result['optB'])
        else:
            result['optB'] = int(result['optB'])
    return result


class SplitBase:
    """
    split_list = {} is dict,the subclass must override it !
    What are the fields that are processed,decide which *_call
    you have put into!
    """
    # Required override
    split_list = {}
    prefix = ''  # You can override it with your name if you like!
    process_function = {
        'is_subpackage': is_subpackage,
        'is_encryption': is_encryption,
        'is_complete': is_complete,
        'is_okay': is_okay
    }

    def __init__(self, val):
        """
        :param val: a tuple (1,2,3,4,5,6,7,8)
        :return:
        """
        self.debug = True
        self.result = {}  # The result of the SplitBase
        if not self.split_list:  # if the subclass no override it, raise a valueError exception!
            raise ValueError("The split_list can't empty!")
        else:
            base_index = 0
            split_list_length = len(self.split_list)
            if val:
                self.message_head_content = val[1:-1]
                self.crc = val[-2]
                if is_complete(self.message_head_content, self.crc):
                    for index in range(split_list_length):
                        spd = split_ruler(self.split_list[index])
                        fill_field = self.prefix + spd['field']
                        if 'fun' in spd:

                            func_object_name = spd['fun']
                            func_object = self.process_function[func_object_name]
                            func_arg_field = self.prefix + spd['arg']
                            func_arg = self.result[func_arg_field]  # Which field you need to checking of the result!
                            if func_object(func_arg):
                                # if you return True ,pick the optA as it's field_range
                                field_range = spd['optA']
                            else:
                                field_range = spd['optB']
                        else:
                            field_range = spd['optA']

                        if isinstance(field_range, list):
                            begin = field_range[0]
                            end = field_range[1]
                            field_value = val[begin:end]
                            split_range = len(field_value)  # The length of the split
                        else:
                            split_range = base_index + field_range  # The field_range here we got a integer !
                            field_value = val[base_index:split_range]

                        base_index = split_range  # increase the index
                        self.result[fill_field] = field_value
                else:
                    # ignore this request from terminal device
                    self.debug = False
                    print 'No complete data from client!'
            else:
                print 'No validation input!'


class SubClassSample(SplitBase):
    """
    You required override the split_list!
    """
    # split_list = {'dev_id': 2, 'tie': 3, 'ghi': 4, 'time': 6}
    split_list = ['dev_id/2', 'tie/2~5', 'ghi/4~-2', 'time/1']
    # prefix = 'ak'


if __name__ == '__main__':
    sample1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19)
    instance1 = SubClassSample(sample1)
    print instance1.result
