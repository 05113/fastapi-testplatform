import requests

url = 'www.baidu.com'

k = 'get'

# a = requests.get(url = url)


response = requests.get(url = 'http://172.31.236.36:7777/api/wes/warehouse/1/parcelcontainer/advancefinish/1' , headers = 'application/json')
# print(a.status_code)