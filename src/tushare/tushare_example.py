import tushare as ts
import pandas as pd

# 1. 初始化接口（替换为你的Token）
ts.set_token('7a4c679ae21b67e10039d6a4b1b9cf405c1bdb493786e41b17f6d91c')
pro = ts.pro_api()

# 2. 获取股票基本信息（如沪深300成分股）
def get_stock_basic():
    # 查询沪深300成分股列表（ts_code为股票代码）
    hs300 = pro.index_weight(index_code='000300.SH', start_date='20230101', end_date='20231231')
    print("沪深300成分股（部分）：")
    print(hs300[['con_code', 'weight']].head())  # con_code为股票代码，weight为权重
    return hs300

# 3. 获取单只股票的日线数据
def get_stock_daily(stock_code='600000.SH', start_date='20230101', end_date='20231231'):
    # 获取日线数据（开盘价、最高价、最低价、收盘价等）
    daily_data = pro.daily(ts_code=stock_code, start_date=start_date, end_date=end_date)
    # 转换日期格式并按时间排序
    daily_data['trade_date'] = pd.to_datetime(daily_data['trade_date'], format='%Y%m%d')
    daily_data = daily_data.sort_values('trade_date')
    print(f"\n{stock_code}日线数据（部分）：")
    print(daily_data[['trade_date', 'open', 'high', 'low', 'close', 'vol']].tail())  # vol为成交量
    return daily_data

# 4. 获取指数行情（如上证指数）
def get_index_data(index_code='000001.SH', start_date='20230101', end_date='20231231'):
    index_data = pro.index_daily(ts_code=index_code, start_date=start_date, end_date=end_date)
    index_data['trade_date'] = pd.to_datetime(index_data['trade_date'], format='%Y%m%d')
    index_data = index_data.sort_values('trade_date')
    print(f"\n{index_code}指数数据（部分）：")
    print(index_data[['trade_date', 'open', 'high', 'low', 'close']].tail())
    return index_data

if __name__ == '__main__':
    # 调用示例
    stock_basic = get_stock_basic()
    daily_data = get_stock_daily(stock_code='600000.SH')  # 浦发银行
    index_data = get_index_data()  # 上证指数
    