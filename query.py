#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request
import re

# debug=True
debug = False


class Utility:
    def ToGB(str):
        if (debug): print(str)
        return str.decode('gb2312')


class StockInfo:
    """
    接口介绍：http://blog.csdn.net/ustbhacker/article/details/8365756
     0: 未知
     1: 名字
     2: 代码
     3: 当前价格
     4: 涨跌
     5: 涨跌%
     6: 成交量（手）
     7: 成交额（万）
     8:
     9: 总市值
     """

    def getStockStrByNum(num):
        f = urllib.request.urlopen('http://qt.gtimg.cn/q=s_' + str(num))
        print('res=', f.read().decode('gbk'))
        res = f.readline()
        f.close()
        return res


    def ParseResultStr(resultstr):
        if (debug): print(resultstr)
        slist = resultstr[14:-3]
        if (debug): print(slist)
        slist = slist.split('~')
        if (debug): print(slist)

        # print('*******************************')
        print('股票名称:', slist[1])
        print('股票代码:', slist[2])
        print('当前价格:', slist[3])
        print('涨    跌:', slist[4])
        print('涨   跌%:', slist[5], '%')
        print('成交量(手):', slist[6])
        print('成交额(万):', slist[7])
        print('总市值:', slist[9])
        # print('date and time is :', dateandtime)
        print('*******************************')

    def GetStockInfo(num):
        str = StockInfo.GetStockStrByNum(num)
        strGB = Utility.ToGB(str)
        StockInfo.ParseResultStr(strGB)

#
# class StockInfoDetail:
#     """
#     接口介绍：http://blog.csdn.net/ustbhacker/article/details/8365756
#      0: 未知
#      1: 名字
#      2: 代码
#      3: 当前价格
#      4: 昨收
#      5: 今开
#      6: 成交量（手）
#      7: 外盘
#      8: 内盘
#      9: 买一
#     10: 买一量（手）
#     11-18: 买二 买五
#     19: 卖一
#     20: 卖一量
#     21-28: 卖二 卖五
#     29: 最近逐笔成交
#     30: 时间
#     31: 涨跌
#     32: 涨跌%
#     33: 最高
#     34: 最低
#     35: 价格/成交量（手）/成交额
#     36: 成交量（手）
#     37: 成交额（万）
#     38: 换手率
#     39: 市盈率
#     40:
#     41: 最高
#     42: 最低
#     43: 振幅
#     44: 流通市值
#     45: 总市值
#     46: 市净率
#     47: 涨停价
#     48: 跌停价
#      """
#
#     def GetStockDetailStrByNum(num):
#         f = urllib.request.urlopen('http://qt.gtimg.cn/q=s_' + str(num))
#         print('res=', f.read().decode('gbk'))
#         res = f.readline()
#         f.close()
#         return res
#
#
#     def ParseDetailResultStr(resultstr):
#         if (debug): print(resultstr)
#         slist = resultstr[14:-3]
#         if (debug): print(slist)
#         slist = slist.split('~')
#         if (debug): print(slist)
#
#         # print('*******************************')
#         print('股票名称:', slist[1])
#         print('股票代码:', slist[2])
#         print('当前价格:', slist[3])
#         print('昨   收:', slist[4])
#         print('今   开:', slist[5])
#         print('成交量(手):', slist[6])
#         print('外盘:', slist[7])
#         print('内盘:', slist[8])
#         print('买一:', slist[9])
#         print('买一量（手）:', slist[10])
#         print('卖一:', slist[19])
#         print('卖一量:', slist[20])
#         print('最近逐笔成交:', slist[29])
#         print('时间:', slist[30])
#         print('涨跌:', slist[31])
#         print('涨跌%:', slist[32])
#         print('最高:', slist[33])
#         print('最低:', slist[34])
#         print('成交量（手）:', slist[36])
#         print('成交额（万）:', slist[37])
#         print('换手率:', slist[38])
#         print('市盈率:', slist[39])
#         print('振幅:', slist[43])
#         print('流通市值:', slist[44])
#         print('总市值:', slist[45])
#         print('市净率:', slist[46])
#         print('涨停价:', slist[47])
#         print('跌停价:', slist[48])
#         # print('date and time is :', dateandtime)
#         print('*******************************')
#
#     def GetStockDetailInfo(num):
#         str = StockInfo.GetStockStrByNum(num)
#         strGB = Utility.ToGB(str)
#         StockInfo.ParseResultStr(strGB)

if __name__ == '__main__':
    code = input("请输入股票代码:")
    no_list = re.findall(r'[0-9]', code)
    no = no_list[0]
    if int(no) == 6:
        code1 = 'sh' + code
        print(code1)
    elif (int(no) == 0) | (int(no) == 3):
        code1 = 'sz' + code
        print(code1)
    else:
        print("请输入正确的股票代码")
    stocks = [code1]
    print("stocks=", stocks)
    for stock in stocks:
        StockInfo.GetStockInfo(stock)
