# -*- coding:utf-8 -*-
import urllib.request


def get_stock(stock_no):
    f = urllib.request.urlopen('http://qt.gtimg.cn/q=s_' + str(stock_no))
    res = f.read().decode('gbk')
    f.close()
    return res


def result_parse(result):
    res_dict = {}
    result_spl = result[14:-3].split('~')
    res_dict['stock_name'] = result_spl[1]
    res_dict['stock_no'] = result_spl[2]
    res_dict['current_price'] = result_spl[3]
    res_dict['fluctuation'] = result_spl[4]
    res_dict['fluctuation_by_percent'] = result_spl[5]
    res_dict['volume'] = result_spl[6]
    res_dict['turnover'] = result_spl[7]
    res_dict['total_value'] = result_spl[9]
    return res_dict


def stock_check(stock_no):
    if len(stock_no) != 6:
        return 0
    no_first = stock_no[0]
    if int(no_first) == 6:
        code = 'sh' + stock_no
        return code
    elif (int(no_first) == 0) | (int(no_first) == 3):
        code = 'sz' + stock_no
        return code
    else:
        return 0