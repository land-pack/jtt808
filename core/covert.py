from utils.timestamp import to_timestamp_fun  # (22, 1, 5, 17, 64, 25) --> 1451965219
from utils.tools import to_double_word_fun  # (2, 110, 226, 147) --> 40.821395
from utils.tools import to_a_word_fun  # (4, 89) --> 1113.0
from utils.tools import to_int_dword_fun  # (6, 168) --> 1704
from visual.visual_decorator import error

# Example :
def to_hello(val):
    return str(val) + 'i am hello func'


class ConvertBase:
    """
    Expect a dict as it's argument!
    """

    # Optional override
    convert_to_WORD_code = []
    convert_to_DWORD_code = []
    convert_to_INT_code = []
    convert_to_timestamp_code = []
    convert_to_hello_code = []
    # Don't need to override
    convert_to_function = {
        'to_word': to_a_word_fun,
        'to_dword': to_double_word_fun,
        'to_int': to_int_dword_fun,
        'to_timestamp': to_timestamp_fun,
        'to_hello': to_hello
    }

    def __init__(self, val):
        self.convert_to_func_arg = {
            'to_word': self.convert_to_WORD_code,
            'to_dword': self.convert_to_DWORD_code,
            'to_int': self.convert_to_INT_code,
            'to_timestamp': self.convert_to_timestamp_code,
            'to_hello': self.convert_to_hello_code
        }
        for func_key in self.convert_to_function:  # Get the static function name
            convert_to_func = self.convert_to_function[func_key]  # Get the static function instance
            convert_lists = self.convert_to_func_arg[func_key]  # Get the target list for deal !
            for each_field in convert_lists:  # Get each item of the list
                if each_field in val:
                    src_data = val[each_field]  # Get the each value from the user input which key is equal each_field!
                    val[each_field] = convert_to_func(src_data)  # convert the result with new value!
                else:
                    error("The Key Does't match any field of val!")


class ConvertBaseSample(ConvertBase):
    convert_to_hello_code = ['bye', 'hey']


if __name__ == '__main__':
    sample = {'to_timestamp': (22, 1, 5, 17, 64, 25), 'bye': (1, 2)}
    print 'old          :', sample
    instance1 = ConvertBaseSample(sample)
    print 'new          :', sample
