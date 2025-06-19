# 环境变量配置指南

## 快速开始

### 方法1：使用自动化脚本（推荐）

```bash
# 运行交互式设置脚本
./setup_env.sh

# 验证配置
python setup_env.py
```

### 方法2：手动配置

1. **复制环境变量模板**
   ```bash
   cp .env.example .env
   ```

2. **编辑.env文件**
   ```bash
   nano .env  # 或使用您喜欢的编辑器
   ```

3. **填入API密钥**
   ```
   # DeepSeek API配置
   OPENAI_API_KEY=sk-your_deepseek_api_key_here
   OPENAI_BASE_URL=https://api.deepseek.com
   
   # FINNHUB API配置
   FINNHUB_API_KEY=your_finnhub_api_key_here
   ```

4. **验证配置**
   ```bash
   python setup_env.py
   ```

## API密钥获取

### DeepSeek API
- 访问：https://platform.deepseek.com
- 注册账户并获取API密钥
- 优势：价格便宜、支持中文、兼容OpenAI格式

### FINNHUB API
- 访问：https://finnhub.io
- 注册免费账户
- 免费计划：60次/分钟调用限制
- 提供股票、财务数据

## 运行项目

配置完成后，选择以下方式运行：

```bash
# CLI界面（推荐）
python -m cli.main

# Python脚本
python main.py

# 使用DeepSeek示例
python deepseek_example.py
```

## 文件说明

- `.env.example` - 环境变量模板文件
- `.env` - 实际的环境变量文件（包含敏感信息，不应提交到git）
- `setup_env.py` - Python环境检查脚本
- `setup_env.sh` - Shell自动化设置脚本
- `deepseek_example.py` - DeepSeek API使用示例

## 安全提醒

⚠️ **重要：** 
- 永远不要将包含真实API密钥的`.env`文件提交到git仓库
- API密钥应当保密，不要在代码中硬编码
- 定期轮换API密钥以确保安全
