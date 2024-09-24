import pandas as pd

# 读取CSV文件
df = pd.read_csv('weatherAUS.csv')

# 提取城市和降雨量列
df = df[['Location', 'Rainfall']]

# 将降雨量列中的'NA'替换为NaN，并转换为浮点数
df['Rainfall'] = pd.to_numeric(df['Rainfall'], errors='coerce')

# 计算每个城市的平均降雨量
average_rainfall = df.groupby('Location')['Rainfall'].mean().reset_index()

# 将结果写入新的CSV文件
average_rainfall.to_csv('average_rainfall.csv', index=False)

print("平均降雨量已保存到average_rainfall.csv")