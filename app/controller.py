# TODO backup code for now
"""
    Input a tuple as it's argument
    """

def build_dict(self,val):
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
