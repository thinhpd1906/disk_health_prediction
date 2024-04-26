from api.constants import MAPPING_DICT
from api.constants import LIST_SMART
import re

class ConvertInput: 
    def convert(self, input: dict):
        smart_convert = {}
        # convert key smart from cmd to smart name of data
        for key, value in input.items():
            if key in MAPPING_DICT:
                smart_convert[MAPPING_DICT[key]] = value
        for item in LIST_SMART:
            if item not in smart_convert:
                smart_convert[item] = 0
        return dict(sorted(smart_convert.items(), key=lambda x: self.custom_sort_key(x[0])))
    
    def custom_sort_key(self, key):
        match = re.match(r'smart_(\d+)_(\w+)', key)
        if match:
            return int(match.group(1)), match.group(2)
        return key
        