import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False 

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'
}

def get_0_7_weather():
    url = 'http://www.weather.com.cn/weather/101020100.shtml'
    resp = requests.get(url, headers=headers)
    resp.encoding = resp.apparent_encoding
    soup = BeautifulSoup(resp.text, 'html.parser')
    result = []
    lis = soup.find_all(class_=re.compile('^sky skyid lv'))
    if lis:
        for li in lis:
            tem = [li.h1.text]
            try:
                rex = re.search('>([+-]*\d+).*?/.*?([+-]*\d+)', str(li.find(class_='tem')), re.S)
                tem.extend([rex.group(1), rex.group(2)])
            except AttributeError:
                t = li.find(class_='tem').i.text[:-1]
                tem.extend([t, t])
            result.append(tem)
        return result
    return get_0_7_weather()

def get_8_15_weather():
    url = 'http://www.weather.com.cn/weather15d/101020100.shtml'
    resp = requests.get(url, headers=headers)
    resp.encoding = resp.apparent_encoding
    soup = BeautifulSoup(resp.text, 'html.parser')
    try:
        result = []
        for li in soup.find(class_='t clearfix').find_all('li'):
            tem = [li.find(class_='time').text]
            rex = re.search('>([+-]*\d+).*?([+-]*\d+)', str(li.find(class_='tem')), re.S)
            tem.extend([rex.group(1), rex.group(2)])
            result.append(tem)
        return result
    except AttributeError:
        get_8_15_weather()

def draw_tem():
    res = get_0_7_weather()
    res.extend(get_8_15_weather())
    res = np.array(res)
    days = res[:, 0]
    tem_max = [int(x) for x in res[:, 1]]
    tem_min = [int(x) for x in res[:, 2]]
    index = np.arange(len(res))
    plt.figure(figsize=(15, 8))
    plt.title('上海市近15天天气预报')
    plt.xlabel('日期')
    plt.ylabel('温度/℃')
    plt.xticks(index, days)
    plt.plot(index, tem_max, color='r', label='最高气温')
    plt.plot(index, tem_min, color='g', label='最低气温')
    for x, y in zip(index, tem_max):
        plt.text(x, y, y)
    for x, y in zip(index, tem_min):
        plt.text(x, y, y)
    plt.legend(loc='upper right')
    plt.savefig('weather.png')
    plt.show()
    

if __name__ == '__main__':
    draw_tem()