import numpy as np
import pandas as pd

data = pd.read_csv('./data/drinks.csv', index_col=0, encoding='gbk')

print('\n查询DataFrame的索引和列')
print(data.index)
print(data.columns)

print('\n查询每个大陆的样本数量')
print(data['continent'].value_counts())

print('\n计算每个大陆红酒的消耗平均值、中位数')
print(data.groupby(data['continent']).mean().loc[:, 'wine_servings'])
print(data.groupby(data['continent']).median().loc[:, 'wine_servings'])

print('\n计算每个大陆spirit饮品消耗的平均值，最大值和最小值')
print(data.groupby(data['continent']).mean().loc[:, 'spirit_servings'])
print(data.groupby(data['continent']).max().loc[:, 'spirit_servings'])
print(data.groupby(data['continent']).min().loc[:, 'spirit_servings'])

print('\n计算哪个大陆(continent)平均消耗的啤酒(beer)最多？')
print(data.groupby(data['continent']).mean().loc[:, 'beer_servings'].idxmax())

print('\n计算每个大陆不同饮料消费量的总和')
print(data.pivot_table(index='continent', values=['beer_servings', 'spirit_servings', 'wine_servings'], aggfunc=np.sum))