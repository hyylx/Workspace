"""
VTEC Quuppa driver
Get interface to Quuppa
author: Xin
date: 11/4/2017
License:
"""

from urllib import request
import json


class VTECQuuppa(object):
    """
    your comment here
    """
    def __init__(self, ip='192.168.0.129'):
        self.ip = ip
        self.tag_id = None

    def set_tag_id(self, tag_id):
        """
        Set your tag id here
        id: int tag number
        """
        self.tag_id = tag_id

    def read_quuppa_tagposition(self):
        with request.urlopen(
                                'http://' +
                                self.ip + ':8080/qpe/getTagPosition?version=2&humanReadable=true&maxAge=2000') as f:
            tagposition_all = f.read()
        return tagposition_all

    def read_quuppa_taginfo(self):
        with request.urlopen(
                                'http://' +
                                self.ip + ':8080/qpe/getTagInfo?version=2&humanReadable=true&maxAge=2000') as f:
            taginfo_all = f.read()
        return taginfo_all

    def get_tag_message(self):
        data = self.read_quuppa_tagposition()
        data_str = data.decode()
        data_dic = json.loads(data_str)
        return data_dic['message']

    def get_location(self):
        """
        get the location of the tag, if you don't set the tag_id this function will return the locations of every tag
        return: [x, y, z]
        """
        data = self.read_quuppa_tagposition()
        data_str = data.decode()
        data_dic = json.loads(data_str)
        return data_dic['tags'][0]['position']

    def get_battery_voltage(self):
        """
        get the battery voltage
        return: float battery voltage
        """
        data = self.read_quuppa_taginfo()
        data_str = data.decode()
        data_dic = json.loads(data_str)
        return data_dic['tags'][0]['batteryVoltage']

    def get_status(self):
        if self.get_battery_voltage():
            pass

        if self.get_location():
            pass

        return "OPERATIONAL"

    def get_diameter(self):
        self.get_location()
        # TODO calculate a diemsion

if __name__ == "__main__":
    test_quppa = VTECQuuppa()
    tag_message = test_quppa.get_battery_voltage()
    print(tag_message)