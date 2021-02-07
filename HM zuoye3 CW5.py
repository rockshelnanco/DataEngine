import pandas as pd
import openpyxl
df = pd.read_csv('./car_complain.csv')
#print(df)
df.to_excel('./car_complain_origin.xlsx',index= False)
df2 = df.join(df.car_model.str.get_dummies(','))    # 基于car_model特征值变化
df2.to_excel('./car_complain_get_dummies.xlsx',index= False)

#print(df2)
#def f(x):
   # x = x.replace('一汽大众','一汽-大众')
   # return x

df3 = df.groupby(['car_model','brand'])['id'].agg(['count'])        #count统计
#print(df3)
df3.to_excel('./car_complain_count.xlsx')
result = df3.sort_values('count')           # 排序
result.to_excel('./car_complain_result.xlsx')