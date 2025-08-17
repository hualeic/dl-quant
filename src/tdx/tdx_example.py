import pandas as pd
import tushare as ts

path = r'D:\new_tdx\T0002\export\SH#600000.txt'

# 读取TXT文件到DataFrame
df = pd.read_csv(
    path,        # TXT文件路径（若不在同一文件夹，需写完整路径，如'C:/files/data.txt'）
    sep='\t',    # 关键：指定分隔符为制表符（Tab），因数据用Tab分隔
    header=1,          # 第一行为表头
    skiprows=[1],      # 跳过第二行（索引1），从第三行开始读数据
    skipfooter=1,      # 忽略最后一行
    engine='python'    # 读取footer需要指定python引擎
)

# 查看结果（可选）
print(df)



