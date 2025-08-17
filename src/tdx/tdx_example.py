import pandas as pd
import tushare as ts
import sys
import os

# 添加src目录到Python路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from logger_config import setup_logger

# 设置日志
logger = setup_logger()

path = r'D:\new_tdx\T0002\export\SH#600000.txt'

# 读取TXT文件到DataFrame
logger.info(f"开始读取文件: {path}")
df = pd.read_csv(
    path,              # TXT文件路径（若不在同一文件夹，需写完整路径，如'C:/files/data.txt'）
    sep='\t',          # 关键：指定分隔符为制表符（Tab），因数据用Tab分隔
    encoding='gbk',    # 指定编码格式，解决中文编码问题
    header=1,          # 第2行为表头
    skiprows=0,        # 不跳过任何行，header=1会自动将第2行作为表头
    skipfooter=1,      # 忽略最后1行
    engine='python'    # 读取footer需要指定python引擎
)

logger.info(f"文件读取完成，数据形状: {df.shape}")
logger.info(f"df: {df}")
