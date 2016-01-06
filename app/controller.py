# TODO backup code for now
"""
    Input a tuple as it's argument
    """

    def __init__(self, val):
        self.exclude_flow = ['alarm', 'status', 'direction']
        self.hash_data = {'alarm': val[0:4],
                          'status': val[4:8],
                          'latitude': val[8:12],
                          'longitude': val[12:16],
                          'altitude': val[16:18],
                          'speed': val[18:20],
                          'direction': val[20:22],
                          'datetime': val[22:28]
                          }
        for item in self.hash_data:
            value = self.hash_data[item]
            value_len = len(value)
            if value_len == 4:
                if item in self.exclude_flow:
                    self.hash_data[item] = to_int_dword_fun(value)
                else:
                    self.hash_data[item] = to_double_word_fun(value)
            elif value_len == 2:
                if item in self.exclude_flow:
                    self.hash_data[item] = to_int_dword_fun(value)
                else:
                    self.hash_data[item] = to_a_word_fun(value)
            elif value_len == 6:
                temp = dec2hex4tuple(value)
                self.hash_data[item] = to_timestamp_fun(temp)
            else:
                print 'There are nothing match the value length!'
