from urllib import request

with request.urlopen('http://192.168.0.142:8080/qpe/getTagPosition?version=2&humanReadable=true&maxAge=5000') as f:
    data = f.read()
    print('Data:', data.decode('utf-8'))

