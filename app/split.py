from core.split import SplitBase


class PositionSplit(SplitBase):
    # Required override the parent attribute
    split_list = ['alarm/4', 'status/4', 'latitude/4',
                  'longitude/4', 'altitude/2', 'speed/2',
                  'direction/2', 'timestamp/6']

    # Optional override
    # prefix = 'my_'


# class TerminalInfoSplit(SplitBase):
#     split_list = ['']
#
#

class TerminalAttributeSplit(SplitBase):
    split_list = ['ter_type/2', 'manuf_id/5', 'ter_model/20',
                  'ter_id/7', 'icc_id/10', 'ter_hardware_v_len/1',
                  'ter_hardware_v/#ter_hardware_v_len',
                  'ter_fixed_v_len/1', 'ter_fixed_v/#ter_fixed_v_len',
                  'gnss/1', 'gnss_attr/1'
                  ]


if __name__ == '__main__':
    sample1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 21, 22, 22, 1, 5, 21, 17, 21)
    instance1 = PositionSplit(sample1)
    print instance1.result
