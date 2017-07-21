# -*- coding:utf-8 -*-
import urllib.request


def get_stock_detail(stock_no):
    """
        接口介绍：http://blog.csdn.net/ustbhacker/article/details/8365756
    """
    # 使用腾讯股票查询接口进行查询
    f = urllib.request.urlopen('http://qt.gtimg.cn/q=' + str(stock_no))
    res = f.read().decode('gbk')
    f.close()
    return res


def result_parse_detail(result):
    res_dict = {}
    result_spl = result[14:-3].split('~')
    res_dict['stock_name'] = result_spl[0]
    res_dict['stock_no'] = result_spl[1]
    res_dict['current_price'] = result_spl[2]
    res_dict['yesterday_close'] = result_spl[3]
    res_dict['today_open'] = result_spl[4]
    res_dict['volume'] = result_spl[5]
    res_dict['outer '] = result_spl[6]
    res_dict['inner'] = result_spl[7]
    res_dict['buy_one'] = result_spl[8]
    res_dict['buy_one_quantity'] = result_spl[9]
    res_dict['sell_one'] = result_spl[18]
    res_dict['sell_one_quantity'] = result_spl[19]
    res_dict['recently_deal'] = result_spl[28]
    res_dict['time'] = result_spl[29]
    res_dict['ups_downs'] = result_spl[30]
    res_dict['ups_downs_percent'] = result_spl[31]
    res_dict['highest'] = result_spl[32]
    res_dict['lowest'] = result_spl[33]
    res_dict['turnover'] = result_spl[35]
    res_dict['volume_transaction'] = result_spl[36]
    res_dict['turnover_rate'] = result_spl[37]
    res_dict['PE_ratio'] = result_spl[38]
    res_dict['amplitude'] = result_spl[42]
    res_dict['market_value'] = result_spl[43]
    res_dict['total_value'] = result_spl[44]
    res_dict['PB'] = result_spl[45]
    res_dict['high_limit'] = result_spl[46]
    res_dict['fall_limit'] = result_spl[47]
    return res_dict


def stock_check_detail(stock_no):
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