from urllib import request
import time
import json

time_count = 0

if  __name__ == "__main__":
    while time_count < 2:
        with request.urlopen('http://192.168.0.142:8080/qpe/getTagPosition?version=2&humanReadable=true&maxAge=2000') as f:
            data = f.read()
            data_str = data.decode()
            # print('Data:', data_str[0])

            data_dic = json.loads(data_str)
            print(data_dic['code'])
            #tags_info = data_dic["tags"][0]
            # print(tags_info['areaID])
            # print('position: ', location)
        time_count += 1
        time.sleep(2)
