'''
Created on 26 Feb 2019

@author: User
'''
import os
script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
rel_path = "/sys/devices/soc0/amba/f8007100.adc/iio:device0"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path)
print(f.read())





