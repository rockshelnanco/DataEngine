import pandas as pd
data = {'name': ['zhangfei', 'guanyu', 'liubei', 'dianwei', 'xuchu'],
        'chineses': [68, 95, 98, 90,  80],
        'mathes': [65, 76, 86, 88, 90],
		'englishes': [30, 98, 88, 77, 90]}

df = pd.DataFrame(data)
print(df)


print(df.mean(axis=0))   #每列平均值
# print(df.mean(axis=1))   #每行平均值
print(df.max(axis=0))    #每列最大值
print(df.min(axis=0))   #每列最小值
print(df.var())#方差
print(df.std())#标准差

print(df.sort_values("chineses"))#基于语文分数排序
print(df.sort_values("mathes"))#基于数学分数排序
print(df.sort_values("englishes"))#基于英语分数排序
