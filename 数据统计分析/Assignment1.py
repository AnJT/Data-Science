import numpy as np
import pandas as pd

data = pd.read_csv('./data/patient_heart_rate.csv', index_col=0, encoding='gbk')
print('\n（1）查看哪些列有缺失值')
print(data.columns[data.isnull().any()])
print(data)

print('\n（2）统一sex列的表示方法：性别用m、f表示')
data['sex'].replace({'男': 'm', '女': 'f'}, inplace=True)
print(data)

print('\n（3）统一wieght列的单位为公斤，然后把“公斤”两个字去掉')
data['weight'] = data['weight'].apply(lambda x: float(x[:-2]) if str(x).endswith('公斤') else float(x[:-1]) / 2)
print(data)

print('\n（4）将第2-4行00~06点间的心率设置为缺失值')
data.loc[2:4,'00~06'] = np.NaN
print(data)

print('\n（5）填充心率缺失值：心率的缺失数据用75填充')
for column in data.columns[4:]:
    data[column].fillna(75, inplace=True)
print(data)

print('\n（6）将前2行设置为缺失值')
data.loc[1:2]=np.nan
print(data)

print('\n（7）删除有缺失值的行')
data.dropna(how='any', axis=0, inplace=True)
print(data)

print('\n（8）查看是否有重复行，如有删除重复行')
print(data.duplicated())
data.drop_duplicates(inplace=True)
print(data)

print('\n（9）“age”列离散化：0~30岁为青少年，31~59岁为中年，60岁及以上为老年。添加一列“age_group”保存离散化后的数据，同时删除“age”列')
bins = [0, 31, 60, 200]
names = ['青少年', '中年', '老年']
data['age_group'] = pd.cut(data['age'], bins, labels=names)
data.drop('age', axis=1, inplace=True)
print(data)

print('\n（10）重新设置索引为连续的整数')
data.reset_index(drop=True,inplace=True)
print(data)
