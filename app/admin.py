# If you want to change your data type,here you go!
from core.covert import ConvertBase


class ConvertBaseRegister(ConvertBase):
    convert_to_timestamp_code = ['timestamp']
    convert_to_DWORD_code = ['longitude', 'latitude']
    convert_to_INT_code = ['alarm', 'status', 'speed', 'direction', 'altitude']
