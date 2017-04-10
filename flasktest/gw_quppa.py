from urllib import request
import time
import json


class VTECQuppaAPI(object):
    def __init__(self, ip='192.168.0.142'):
        self.ip = ip

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


if __name__ == "__main__":
    new_quppa = VTECQuppaAPI()
    new_quppa.get_location()
    time.sleep(3)
    new_quppa.get_location()