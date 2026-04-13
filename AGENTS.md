# AGENTS.md - AI 编码代理指南

## 项目概述

**dl-quant** 是一个基于 Python 的量化交易数据工具集，集成了 Tushare、聚宽 (JQDataSDK)、通达信 (TDX) 等多个 A 股数据源，用于行情数据获取与分析。

## 技术栈

- **语言**: Python 3.10
- **包管理**: pip
- **核心依赖**: tushare, jqdatasdk, pandas

## 项目结构

```
dl-quant/
├── src/
│   ├── tushare/          # Tushare 数据接口模块
│   ├── tdx/              # 通达信数据解析模块
│   ├── join_quant/       # 聚宽数据接口模块
│   └── logger_config.py  # 日志配置
├── requirements.txt      # Python 依赖
├── pyproject.toml        # 项目元数据与工具配置
├── .env.example          # 环境变量模板
└── .gitignore
```

## 开发命令

```bash
# 安装依赖
pip install -r requirements.txt

# 运行指定模块
python -m src.tushare.tushare_example
python -m src.tdx.tdx_example

# 代码检查（需安装对应工具）
ruff check src/
# 或
flake8 src/

# 代码格式化
ruff format src/
# 或
black src/
```

## 编码规范

- 领域相关逻辑（股票术语等）使用**中文注释**
- 遵循 **PEP 8** 代码风格
- 生产代码使用 `logging` 模块（通过 `src/logger_config.py`），避免使用 `print()`
- **禁止在源码中硬编码凭据**，通过 `.env` 文件使用环境变量
- 函数签名使用类型注解
- 模块导入使用基于 `src` 包的绝对路径

## 环境变量

敏感凭据必须存放在 `.env` 文件中（不提交到 git）。所需变量参见 `.env.example`：

- `TUSHARE_TOKEN` - Tushare API 令牌
- `JQDATA_USERNAME` - 聚宽账号用户名
- `JQDATA_PASSWORD` - 聚宽账号密码

## 注意事项

- `src/` 目录是 Python 包，导入模块时使用 `from src.xxx import yyy`
- 数据文件（CSV、TXT 等）不应提交到 git
- TDX 模块读取通达信本地导出目录中的文件
