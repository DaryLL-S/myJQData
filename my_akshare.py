# -*- coding: utf-8 -*-
# @Time    : 2022/3/1 22:43
# @Author  : Daryl
# @FileName: my_akshare.py
# @Software: PyCharm

import csv
import os
import time

import akshare as ak
from datetime import datetime as dt
import re
import pandas as pd
# df = get_all_securities(types=['stock'], date='2017-01-01')
date_start = dt.strptime('2017-01-01', '%Y-%m-%d')
date_end = dt.strptime('2021-12-31', '%Y-%m-%d')


# 获取上市股票列表
def my_list():
    stock_list = ak.stock_zh_a_spot_em()
    print(stock_list)
    df = stock_list[['代码', '名称']]
    df.to_csv("stock_list.csv")

    stock_list = ak.stock_zh_a_spot()
    print(stock_list)
    df = stock_list[['代码', '名称']]
    df.to_csv("stock_list2.csv")


# 获取股票历史行情数据
def my_stock():
    filePath = "stock"
    with open("stock_list.csv", 'r', encoding='utf-8', newline='') as rf:
        reader = csv.DictReader(rf)
        file = []
        for i, j, k in os.walk(filePath):
            for s in k:
                fileName = re.sub('\.csv', '', s)
                file.append(fileName)
        for row in reader:
            if row['代码'] not in file:
                stock_individual_info_em_df = ak.stock_individual_info_em(symbol=row['代码'])
                print(stock_individual_info_em_df)

                if stock_individual_info_em_df.iloc[3, 1] != '-':
                    market_date = dt.strptime(str(stock_individual_info_em_df.iloc[3, 1]), "%Y%m%d")
                    if market_date < date_end:
                        if stock_individual_info_em_df.iloc[0, 1] != '-':
                            stock = ak.stock_zh_a_hist(symbol=row['代码'], period="daily", start_date="20000101",
                                                       end_date='20211231', adjust="hfq")
                            stock.to_csv(f"stock/{row['代码']}.csv")
                            print(row['代码'], "store")
                        else:
                            print(row['代码'], "pass")
                    else:
                        print(row['代码'], "pass")
                else:
                    print(row['代码'], "pass")
                time.sleep(1)


# 获取股票指数数据
def my_stock_index():
    # stock_zh_index_daily_df = ak.stock_zh_index_daily(symbol="sh000001")
    # print(stock_zh_index_daily_df)
    # stock_zh_index_daily_df.to_csv("stock_index/sh000001.csv")
    # stock_zh_index_hist_csindex_df = ak.stock_zh_index_hist_csindex(symbol="H30374", start_date="20090101",
    #                                                                 end_date="20211231")
    # print(stock_zh_index_hist_csindex_df)
    # stock_zh_index_hist_csindex_df.to_csv("stock_index/H30374.csv")
    # filePath = "index"
    # with open("all_index.csv", 'r', encoding='utf-8', newline='') as rf:
    #     reader = csv.DictReader(rf)
    #     file = []
    #     for i, j, k in os.walk(filePath):
    #         for s in k:
    #             fileName = re.sub('\.csv', '', s)
    #             file.append(fileName)
    #     for row in reader:
    #         if row['指数代码'] not in file:
    #             print(row['指数代码'])
    #             index_hist_cni_df = ak.index_hist_cni(symbol=row['指数代码'])
    #             print(index_hist_cni_df)
    #             index_hist_cni_df.to_csv(f"index/{row['指数代码']}.csv")
    index_hist_cni_df = ak.index_hist_cni(symbol='H30374')
    print(index_hist_cni_df)
    index_hist_cni_df.to_csv(f"index/'H30374'.csv")


# 获取全部指数数据
def all_index():
    index_all_cni_df = ak.index_all_cni()
    print(index_all_cni_df)
    index_all_cni_df.to_csv("all_index.csv")


# get China rate data
def China_rate():
    macro_bank_china_interest_rate_df = ak.macro_bank_china_interest_rate()
    print(macro_bank_china_interest_rate_df)
    macro_bank_china_interest_rate_df.to_csv("interest_rate/China_bank_interest_rate.csv")


def stock_indicator():
    filePath = "stock_indicator"
    with open("stock_list.csv", 'r', encoding='utf-8', newline='') as rf:
        reader = csv.DictReader(rf)
        file = []
        for i, j, k in os.walk(filePath):
            for s in k:
                fileName = re.sub('\.csv', '', s)
                file.append(fileName)
        for row in reader:
            if row['代码'] not in file:
                try:
                    stock_a_lg_indicator_df = ak.stock_a_lg_indicator(symbol=row['代码'])
                    stock_a_lg_indicator_df.to_csv(f"stock_indicator/{row['代码']}.csv")
                except:
                    continue


def bond():
    bond_zh_hs_daily_df = ak.bond_zh_hs_daily(symbol="sz127003")
    print(bond_zh_hs_daily_df)
    bond_zh_hs_daily_df.to_csv('bond/sz127003.csv')


if __name__ == '__main__':
    # my_stock_index()
    # my_list()
    # stock_indicator()
    bond()

















        # print(row['code'])
        # d_start = dt.strptime(row['start_date'], '%Y-%m-%d')
        # d_end = dt.strptime(row['end_date'], '%Y-%m-%d')
        # T = re.sub('\..*', '', row['code'])

#         if d_start < date_start and d_end > date_end:
#             print(1)
#             stock = ak.stock_zh_a_hist(symbol=T, period="daily", start_date="20170101", end_date='20211231', adjust="hfq")
#             stock.to_csv(f"stock/{T}.csv")
#         elif d_start > date_start and d_end > date_end:
#             print(2)
#             str = d_start.strftime("%Y-%m-%d")
#             str = re.sub('-', '', str)
#             stock = ak.stock_zh_a_hist(symbol=T, period="daily", start_date=str, end_date='20211231',
#                                        adjust="hfq")
#             stock.to_csv(f"stock/{T}.csv")
#         elif d_start < date_start and d_end < date_end:
#             print(3)
#             str = d_end.strftime("%Y-%m-%d")
#             str = re.sub('-', '', str)
#             print(str)
#             print(type(str))
#             stock = ak.stock_zh_a_daily(symbol=T, start_date="20170101", end_date=str, adjust="hfq")
#             # stock = ak.stock_zh_a_hist(symbol=T, period="daily", start_date="20170101", end_date=str,
#             #                            adjust="hfq")
#             stock.to_csv(f"stock/{T}.csv")
#         else:
#             print(4)
#             str1 = d_start.strftime("%Y-%m-%d")
#             str1 = re.sub('-', '', str1)
#             str2 = d_end.strftime("%Y-%m-%d")
#             str2 = re.sub('-', '', str2)
#             stock = ak.stock_zh_a_hist(symbol=T, period="daily", start_date=str1, end_date=str2,
#                                        adjust="hfq")
#             stock.to_csv(f"stock/{T}.csv")

