#!/bin/bash
# TradingAgents 环境变量设置脚本

echo "🔧 TradingAgents 环境变量设置"
echo "================================"

# 检查是否存在.env文件
if [ ! -f ".env" ]; then
    echo "📝 创建 .env 文件..."
    cp .env.example .env
    echo "✅ 已创建 .env 文件"
fi

echo ""
echo "📋 请填入以下API密钥到 .env 文件中:"
echo ""

# 读取用户输入
read -p "🔑 请输入DeepSeek API密钥 (从 https://platform.deepseek.com 获取): " DEEPSEEK_KEY
read -p "🔑 请输入FINNHUB API密钥 (从 https://finnhub.io 获取): " FINNHUB_KEY

# 更新.env文件
if [ -n "$DEEPSEEK_KEY" ]; then
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        sed -i '' "s/OPENAI_API_KEY=.*/OPENAI_API_KEY=$DEEPSEEK_KEY/" .env
    else
        # Linux
        sed -i "s/OPENAI_API_KEY=.*/OPENAI_API_KEY=$DEEPSEEK_KEY/" .env
    fi
    echo "✅ 已设置DeepSeek API密钥"
fi

if [ -n "$FINNHUB_KEY" ]; then
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        sed -i '' "s/FINNHUB_API_KEY=.*/FINNHUB_API_KEY=$FINNHUB_KEY/" .env
    else
        # Linux
        sed -i "s/FINNHUB_API_KEY=.*/FINNHUB_API_KEY=$FINNHUB_KEY/" .env
    fi
    echo "✅ 已设置FINNHUB API密钥"
fi

echo ""
echo "🎉 环境变量设置完成！"
echo ""
echo "🚀 现在可以运行项目了:"
echo "   python setup_env.py  # 验证配置"
echo "   python -m cli.main   # 运行CLI界面"
echo "   python main.py       # 运行Python脚本"
