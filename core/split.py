class SplitBase:
    """
    split_list = {} is dict,the subclass must override it !
    What are the fields that are processed,decide which *_call
    you have put into!
    """
    # Required override
    split_list = {}

    def __init__(self, val):
        """
        :param val: a tuple (1,2,3,4,5,6,7,8)
        :return:
        """
        self.result = {}

        if not self.split_list:  # if the subclass no override it, raise a valueError exception!
            raise ValueError("The split_list can't empty!")
        else:
            base_index = 0
            for key in self.split_list:
                split_range = base_index + self.split_list[key]
                self.result[key] = val[base_index:split_range]
                base_index = split_range


class SubClassSample(SplitBase):
    """
    You required override the split_list!
    """
    split_list = {'dev_id': 2, 'tie': 3, 'ghi': 4, 'time': 6}


if __name__ == '__main__':
    sample1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 22, 1, 5, 17, 64, 25)
    instance1 = SubClassSample(sample1)
    print instance1.result
