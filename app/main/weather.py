# -*- coding:utf-8 -*-
import json
import urllib.parse
import urllib.request


def get_city(city):
    '''
    请求地址：http://v.juhe.cn/weather/index
    请求参数：cityname=%E5%A4%A7%E8%BF%9E&dtype=&format=&key=yourKey
    请求方式：GET
    '''
    # city = input('请输入城市名:')
    code_uri = "http://v.juhe.cn/weather/index"

    parameter = urllib.parse.urlencode(
        {"cityname": city, "dtype": "json", "format": "1", "key": "251b4402fb74eec9b22aa3c65c0dcf74"})

    # total
    uri = code_uri + "?" + parameter

    # 通过json模块来读取上面接口打开后返回的数据，并解码
    ret = json.loads(urllib.request.urlopen(uri).read().decode("utf-8"))

    return ret


def weather_query(ret):

    if ret['error_code'] != 0:  # 如果错误代码不为0
        print(ret['reason'])  # 则打印原因
        print(ret['error_code'])  # 和具体哪个故障点
        return (ret['reason'], ret['error_code'])
    else:
        print(ret['reason'])  # 如果没有错误，打印生成结果

        data = json.dumps(ret['result'], sort_keys=True, indent=4, separators=(',', ': '))

        return data


# if __name__=="__main__":
#     test = get_city()
#     weather_query(test)
