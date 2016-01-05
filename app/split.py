from utils.tools import to_bcd
from utils.tools import to_timestamp
from utils.tools import to_double_word
from utils.tools import to_a_word


class PositionSplit:
    """
    Input a tuple as it's argument
    """

    def __init__(self, val):
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
                self.hash_data[item] = to_double_word(value)
            elif value_len == 2:
                self.hash_data[item] = to_a_word(value)
            elif value_len == 6:
                temp = to_bcd(value)
                self.hash_data[item] = to_timestamp(temp)
            else:
                print 'There are nothing match the value length!'


if __name__ == '__main__':
    sample1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 21, 22, 22, 1, 5, 21, 17, 21)
    instance1 = PositionSplit(sample1)
    print instance1.hash_data
