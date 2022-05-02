import numpy as np
import pandas as pd

data_user = pd.read_csv('./data/users.csv', encoding='gbk')
data_order = pd.read_csv('./data/orders.csv', encoding='gbk')

data = pd.merge(data_user, data_order, how='inner', on='客户编号')
print(data)

print('\n（1）查看user_order的行索引、列索引、各列的数据类型')
print('行索引:', data.index)
print('列索引:', data.columns)
print('各列数据类型:')
for column in data.columns:
    print(column, data[column].dtype)

print('\n（2）查看订了“过桥米线”的客户的姓名')
print(data.loc[data['品名'] == '过桥米线', '姓名'].unique())

print('\n（3）查看哪些客户在 “云海肴”或者“丰收日”订了餐')
print(data.loc[data['商家'].isin(['云海肴', '丰收日']), '姓名'].unique())

print('\n（4）为user_order增加“小计”列，小计=数量单价')
data['小计'] = data['数量'] * data['单价']
print(data)

print('\n（5）计算每位客户的订餐总金额和所有订单的总金额')
print(data.groupby('姓名')['小计'].sum())
print('所有订单的总金额:', data['小计'].sum())

print('\n（6）计算每个商家的订单数量和订单的平均金额')
print(data['商家'].value_counts())
print(data.groupby('商家')['小计'].mean())

print('\n（7）输出订单来自哪些商家(重复的只输出一次,unique)')
print(data['商家'].unique())

print('\n（8）将“姓名、品名、数量、小计”四列的数据按“小计”降序排序后，写入文件out.csv')
data.sort_values(by='小计',ascending=False, inplace=True)
print(data)
data.to_csv('./out.csv', columns=['姓名', '品名', '数量', '小计'], index=None, encoding='gbk')
