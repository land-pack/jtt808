from utils.tools import is_subpackage
from utils.tools import is_encryption
from utils.tools import is_complete
from visual.visual_decorator import error
import re


def is_true(val):
    """
    :param val: A string
    :return: BOOL type
    """
    print 'output by is_okay:', val
    return True


def filer_wave_line(val):
    temp = val.split('~')
    result = [int(x) for x in temp]
    return result


def build_dict(val):
    """
    :param val: It's a string with some ruler Example: 'foo/is_true(bar)1~2?1~4'
    :return: {'field':'foo','fun':'is_true','arg':'bar','optA':'1~2','optB':'1~4'}
    """
    if '?' in val:  # If you split_list have something like this Example# 'tie/is_okay(dev_id)?1~2:2~4'
        pattern = re.compile(r'(?P<field>.*)/(?P<fun>.*)\((?P<arg>.*)\)\?(?P<optA>.*):(?P<optB>.*)')
    else:
        if ':' in val:  # If you split_list have something like this Example# 'tie/1~2:1~4'
            pattern = re.compile(r'(?P<field>.*)/(?P<optA>.*):(?P<optB>.*)')
        else:  # If you split_list have something like this Example# 'tie/1'
            if '#' in val:
                pattern = re.compile(r'(?P<field>.*)/#(?P<pre_field>.*)')
            else:
                pattern = re.compile(r'(?P<field>.*)/(?P<optA>.*)')
    m = pattern.match(val)
    return m.groupdict()


def rebuild_dict(val):
    """
    :param val: It's a dict type Example : {'optA':1~3,'optB':1~5}
    :return: {'fun': 'is_true', 'field': 'foo', 'arg': 'bar', 'optA': [1, 3], 'optB': [1, 5]}
    """
    if 'optA' in val:
        if '~' in val['optA']:
            val['optA'] = filer_wave_line(val['optA'])
        else:
            val['optA'] = int(val['optA'])
    if 'optB' in val:
        if '~' in val['optB']:
            val['optB'] = filer_wave_line(val['optB'])
        else:
            val['optB'] = int(val['optB'])
    return val


def split_ruler(val):
    temp = build_dict(val)
    result = rebuild_dict(temp)
    return result


class SplitBase:
    """
    split_list = {} is dict,the subclass must override it !
    What are the fields that are processed,decide which *_call
    you have put into!
    """
    # Required override
    split_list = {}
    crc_check = False  # If you Split the message content only! just set it False
    prefix = ''  # You can override it with your name if you like!
    process_function = {
        'is_subpackage': is_subpackage,
        'is_encryption': is_encryption,
        'is_complete': is_complete,
        'is_true': is_true
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
        if val:

            if self.crc_check:
                self.message_head_content = val[1:-1]
                self.crc = val[-2]
                if is_complete(self.message_head_content, self.crc):
                    self.build_dict(val)
                else:
                    # ignore this request from terminal device
                    self.debug = False
                    error('No complete data from client!')
            else:
                self.build_dict(val)
        else:
            error('No validation input!')

    def build_dict(self, val):
        base_index = 0
        split_list_length = len(self.split_list)

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
                if 'pre_field' in spd:
                    pre_field_name = spd['pre_field']
                    pre_field_value = self.result[pre_field_name]
                    spd['optA'] = pre_field_value[0]
                    field_range = spd['optA']
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


class SubClassSample(SplitBase):
    """
    You required override the split_list!
    The below split_list is very easy to understand,let me tell you
    how it's funny!
    Example Data: (3, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19)
    'bar/1' --> {'bar':3}
    'foo/is_true(bar)?1~3:1~5'  --> {'foo':(2,3} # Because is_true return true!
    'sap/#bar' --> {'sap':(5,6,7)}  # Because # mean according the bar field check!(3 length)
    """
    # split_list = {'dev_id': 2, 'tie': 3, 'ghi': 4, 'time': 6}
    split_list = ['bar/1', 'foo/is_true(bar)?1~3:1~5', 'sap/#bar', 'time/1']
    # prefix = 'ak'


if __name__ == '__main__':
    sample1 = (3, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19)
    instance1 = SubClassSample(sample1)
    print instance1.result
