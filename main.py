# importing libraries
import os
import pandas as pd
from pandas import ExcelWriter
from api.convert_input import ConvertInput
import numpy as np
from core.model import Model
# import os
# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0import tensorflow as tf

from tensorflow import keras
model = keras.models.load_model("C:/Users/phant/Downloads/my_model2.keras")
a=[[2.96745900e+006, 1.12000000e+002, 4.67516560e+007, 1.29311363e+002
, 7.54763536e+001, 9.20000000e+001, 0.00000000e+000, 1.00000000e+002
, 9.00000000e+000, 1.00000000e+002, 0.00000000e+000, 8.80000000e+001
, 3.96898888e-315, 1.16337069e+002, 2.94678325e+001, 7.30000000e+001
, 2.43850000e+004, 1.00000000e+002, 0.00000000e+000, 1.00000000e+002
, 9.00000000e+000, 1.00000000e+002, 0.00000000e+000, 1.00000000e+002
, 0.00000000e+000, 1.00000000e+002, 0.00000000e+000, 1.00000000e+002
, 0.00000000e+000, 9.80000000e+001, 2.00000000e+000, 7.70000000e+001
, 2.30000000e+001, 1.00000000e+002, 0.00000000e+000, 1.00000000e+002
, 4.00000000e+000, 9.50000000e+001, 1.09340000e+004, 2.30000000e+001
, 2.30000000e+001, 1.12217457e+002, 1.90673682e+000, 1.00000000e+002
, 2.40000000e+001, 1.00000000e+002, 2.40000000e+001, 2.00000000e+002
, 0.00000000e+000, 1.00000000e+002, 1.20245697e-319, 1.00000000e+002
, 1.38359033e-313, 1.00000000e+002, 6.71608546e-313],
       [2.72050400e+006, 1.19000000e+002, 2.11811224e+008,
        1.29311363e+002, 7.54763536e+001, 9.70000000e+001,
        0.00000000e+000, 1.00000000e+002, 3.00000000e+000,
        1.00000000e+002, 0.00000000e+000, 8.40000000e+001,
        1.46546392e-315, 1.16337069e+002, 2.94678325e+001,
        9.20000000e+001, 7.73600000e+003, 1.00000000e+002,
        0.00000000e+000, 1.00000000e+002, 3.00000000e+000,
        1.00000000e+002, 0.00000000e+000, 1.00000000e+002,
        0.00000000e+000, 1.00000000e+002, 0.00000000e+000,
        1.00000000e+002, 0.00000000e+000, 1.00000000e+002,
        0.00000000e+000, 7.60000000e+001, 2.40000000e+001,
        1.00000000e+002, 0.00000000e+000, 1.00000000e+002,
        0.00000000e+000, 7.70000000e+001, 4.60690000e+004,
        2.40000000e+001, 2.40000000e+001, 1.12217457e+002,
        1.90673682e+000, 1.00000000e+002, 0.00000000e+000,
        1.00000000e+002, 0.00000000e+000, 2.00000000e+002,
        0.00000000e+000, 1.00000000e+002, 3.67090775e-320,
        1.00000000e+002, 1.26620517e-313, 1.00000000e+002,
        5.09321521e-314]]
a_array = np.array(a)
# class to hold all the
# details about the device
class Device():
 
    def __init__(self):
 
        self.device_name = None
        self.info = {}
        self.results = []
        self.smart = {}
 
    # get the details of the device
    def get_device_name(self):
 
        cmd = 'smartctl --scan'
 
        data = os.popen(cmd)
        res = data.read()
        temp = res.split(' ')
        temp = temp[0].split('/')
        name = temp[2]
        self.device_name = name
 
 
    # get the device info (sda or sdb)
    def get_device_info(self):
        cmd = 'smartctl -i /dev/' + self.device_name
        data = os.popen(cmd)
        res = data.read().splitlines()
        device_info = {}
 
        for i in range(4, len(res) - 1):
            line = res[i]
            temp = line.split(':')
            device_info[temp[0]] = temp[1]
        self.info = device_info
    
    def get_smart_infor(self):
        cmd = 'smartctl -a /dev/' + self.device_name 
        data = os.popen(cmd)
        res = data.read().splitlines()
        index = res.index('=== START OF SMART DATA SECTION ===')
        disk_smart = {}
        for i in range((index+4), len(res)):
            if(res[i] == ''):
                break;
            line = res[i]
            temp = line.split(':')
            disk_smart[temp[0]] = temp[1].strip()
        self.smart = self.handle_smart_value(disk_smart)

    def handle_smart_value(self, disk_smart: dict):
        smart_handled = {}
        for key, value in disk_smart.items():
            if "," in value:
                value = value.replace(',', '')
            if key == "Temperature":
               temp = value.split(' ')
               smart_handled[key] = int(temp[0])
            elif key == "Host Read Commands":
                smart_handled[key] = int(value)
            elif key == "Host Write Commands":
                smart_handled[key] = int(value)
            elif key == "Power Cycles":
                smart_handled[key] = int(value)
            elif key == "Power On Hours":
                smart_handled[key] = int(value)
            else:
                smart_handled[key] = value
        return smart_handled
            

    # save the results as an excel file
   
 
 
# driver function
if __name__ == '__main__':
    device = Device()
    model = Model()
    device.get_device_name() 
    device.get_smart_infor()  
    convertInput = ConvertInput()
    # print(device.smart)
    smart_infor = convertInput.convert(device.smart)
    a = model.predict(smart_infor)


