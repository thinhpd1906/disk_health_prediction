from api.constants import MAPPING_DICT, LIST_SMART, SMART_MAP_STANDARD

import re

class ConvertInput: 
    def convert(self, input: dict):
        smart_convert = {}
        smart_important = {}
        # convert key smart from cmd to smart name of data
        for key, value in input.items():
            if key in MAPPING_DICT:
                smart_convert[MAPPING_DICT[key]] = value
        for key, value in smart_convert.items():
            if key in SMART_MAP_STANDARD:
                smart_important[SMART_MAP_STANDARD[key]] = value
        for item in LIST_SMART:
            if item not in smart_convert:
                smart_convert[item] = 0
        for key, value in SMART_MAP_STANDARD.items():
            if value not in smart_important:
                smart_important[value] = -999

        return dict(sorted(smart_convert.items(), key=lambda x: self.custom_sort_key(x[0]))), smart_important
    
    def custom_sort_key(self, key):
        match = re.match(r'smart_(\d+)_(\w+)', key)
        if match:
            return int(match.group(1)), match.group(2)
        return key
        