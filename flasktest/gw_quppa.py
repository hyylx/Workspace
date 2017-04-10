"""
VTEC Quppa driver
Get interface to Quppa
author: Xin
date:
License:
"""

from urllib import request
import time
import json


class VTECQuppa(object):
    """
    your comment here
    """
    def __init__(self, ip='192.168.0.142'):
        self.ip = ip
        self.tag_id = None

    def set_tag_id(self, id):
        """
        Set your tag id here
        id: int tag number
        """
        self.tag_id = id

    def get_location(self):
        with request.urlopen(
                                'http://' +
                                self.ip + ':8080/qpe/getTagPosition?version=2&humanReadable=true&maxAge=2000') as f:
            data = f.read()
            data_str = data.decode()
            # print('Data:', data_str[0])

            data_dic = json.loads(data_str)
            print(data_dic['code'])
            # tags_info = data_dic["tags"][0]
            # print(tags_info['areaID])
            # print('position: ', location)

    def read_quppa(self):
        pass

    def get_battery_voltage(self):
        pass

    def get_status(self):
        if self.get_battery_voltage():
            pass

        if self.get_location():
            pass

        return "OPERATIONAL"

    def get_diameter(self):
        self.get_location()
        #TODO calculate a diemsion

if __name__ == "__main__":
    new_quppa = VTECQuppa()
    new_quppa.set_tag_id(2)
    new_quppa.get_location()
    time.sleep(3)
    new_quppa.get_location()
    new_quppa.get_diameter()
    new_quppa.get_battery_voltage()
