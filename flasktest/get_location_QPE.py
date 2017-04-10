from urllib import request
import time

time_count = 0
while time_count < 5:
    with request.urlopen('http://192.168.0.142:8080/qpe/getTagPosition?version=2&humanReadable=true&maxAge=2000') as f:
        data = f.read()
        print('Data:', data.decode('utf-8'))
    time_count += 1
    time.sleep(3)
