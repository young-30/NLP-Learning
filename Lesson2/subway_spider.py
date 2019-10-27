import requests
from bs4 import BeautifulSoup
import re
import os
 
url = 'https://www.bjsubway.com/station/zjgls/#'


def get_response():
	requests.packages.urllib3.disable_warnings() # 使用verify=False后加上该配置，避免报错
	response = requests.get(url, verify=False) # verify=False用于关闭SSL验证
	response.encoding = 'gbk'  # 原始网页编码错误，没有使用utf-8，只能用gbk
	html = response.text  # 接收response内容
	return BeautifulSoup(html, 'lxml')


def get_stationinfo():
    soup = get_response()
    Stationinfo = soup.find_all('tbody')
    obj = []
    for each in Stationinfo:
        temp = re.findall(r">(.+?)<", str(each))
        obj += temp
    return obj


# 把数据写入.txt文件
def file_op(): 
	os.makedirs('./data/', exist_ok=True)
	station_list = get_stationinfo()
	if station_list:
		with open('./data/subway_station2.txt', 'w', encoding='utf8') as f:  # 不能是wb，编码有问题，或者str转换成byte; 指定为UTF8，这样后面读取数据时可以正确解码
		    for line in station_list:
		        if line == '上行/下行':
		            f.write(line + '\n')
		        else:
		            f.write(line + '      ')  


file_op()



