import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']='SimHei'

data = pd.read_csv('./data/titanic.csv', encoding='gbk')

print('\n将passage设置为索引')
data.set_index('PassengerId', inplace=True)
print(data)

print('\n船上共多少名乘客？其中男性、女性各多少人？绘制扇形图展示男女比例')
print(data.shape[0])
print(data['Sex'].value_counts())
plt.pie(data['Sex'].value_counts().values, labels=['male', 'female'], autopct='%.2f%%')
plt.title('男女比例')
plt.show()

print('\n多少人生还？用交叉表显示生还和非生还的不同仓位的人数')
print(data['Survived'].value_counts()[1])
print(pd.crosstab(index=data["Survived"], columns=data["Cabin"]))

print('\n绘制一个展示船票价格的直方图')
bins = np.arange(0, data['Fare'].max(), 2)
plt.hist(data['Fare'].values, bins, color='k')
plt.xlim(0,data['Fare'].max(),50)
plt.xlabel("船票价格")
plt.ylabel("统计数量")
plt.title("船票直方图")
plt.show()

print('\n将数据集按照‘Fare’降序排序后，保存至本地')
data.sort_values(by='Fare', inplace=True, ascending=False)
print(data['Fare'])
data.to_csv('./data/titanic_sort_by_fare_desc.csv', encoding='gbk')
