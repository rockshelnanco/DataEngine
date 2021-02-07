#三国武将分数统计，使用numpy 或 pandas

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


'''import numpy as np

def homework():
	persontype = np.dtype({'names':['name', 'chinese', 'math', 'english'], \
							'formats':['S32','i', 'i', 'i', ]})  #S32表示32字节长度的字符串，i表示32位的整数，f表示32位长度的浮点数。
	peoples = np.array([("ZhangFei",68,65,30),("GuanYu",95,76,98), \
						("LieBei",98,86,88),("DianWei",90,88,77),("XuChu",90,88,77)], dtype=persontype)
	chineses = peoples['chinese']
	maths = peoples['math']
	englishs = peoples['english']

	print("语文平均分:",np.mean(chineses))
	print("语文最大成绩:", np.max(chineses))
	print("语文最小成绩:",np.min(chineses))
	print("语文标准差:", np.std(chineses, ddof=1))
	print("语文方差:", np.var(chineses))

	print("数学平均分:",np.mean(maths))
	print("数学最大成绩:", np.max(maths))
	print("数学最小成绩:", np.min(maths))
	print("数学标准差:", np.std(maths, ddof=1))
	print("数学方差:", np.var(maths))

	print("英语平均分:",np.mean(englishs))
	print("英语最大成绩:", np.max(englishs))
	print("英语最小成绩:", np.min(englishs))
	print("英语标准差:", np.std(englishs, ddof=1))
	print("英语方差:", np.var(englishs))

homework()'''