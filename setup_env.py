#!/usr/bin/env python3
"""
环境变量加载和验证脚本
用于TradingAgents项目的API密钥管理
"""

import os
import sys
from dotenv import load_dotenv
from pathlib import Path

def load_environment():
    """加载环境变量文件"""
    # 查找.env文件
    env_path = Path('.env')
    
    if env_path.exists():
        load_dotenv(env_path)
        print("✅ 已加载 .env 文件")
    else:
        print("⚠️  未找到 .env 文件，将使用系统环境变量")

def validate_api_keys():
    """验证必需的API密钥是否已设置"""
    required_keys = {
        'OPENAI_API_KEY': 'DeepSeek API密钥（或OpenAI API密钥）',
        'FINNHUB_API_KEY': 'FINNHUB API密钥'
    }
    
    missing_keys = []
    
    for key, description in required_keys.items():
        value = os.getenv(key)
        if not value or value.strip() == '' or 'your_' in value.lower():
            missing_keys.append(f"  • {key}: {description}")
            print(f"❌ 缺少 {key}")
        else:
            # 只显示前几位和后几位字符，中间用*代替
            masked_value = f"{value[:4]}...{value[-4:]}" if len(value) > 8 else "***"
            print(f"✅ {key}: {masked_value}")
    
    if missing_keys:
        print("\n🚨 缺少以下必需的API密钥:")
        for key in missing_keys:
            print(key)
        print("\n📝 请按以下步骤配置:")
        print("1. 编辑 .env 文件")
        print("2. 填入您的实际API密钥")
        print("3. 重新运行此脚本验证")
        return False
    
    return True

def show_api_info():
    """显示API获取信息"""
    print("\n📚 API密钥获取指南:")
    print("┌─ DeepSeek API:")
    print("│  • 网站: https://platform.deepseek.com")
    print("│  • 注册并获取API密钥")
    print("│  • 价格相对便宜，支持中文")
    print("│")
    print("├─ FINNHUB API:")
    print("│  • 网站: https://finnhub.io")
    print("│  • 免费计划: 60次/分钟")
    print("│  • 提供股票和金融数据")
    print("└─")

def show_current_config():
    """显示当前配置"""
    print("\n⚙️  当前配置:")
    print(f"  • BASE_URL: {os.getenv('OPENAI_BASE_URL', '默认')}")
    print(f"  • 工作目录: {os.getcwd()}")

def main():
    """主函数"""
    print("🔧 TradingAgents 环境配置检查器")
    print("=" * 50)
    
    # 加载环境变量
    load_environment()
    
    # 显示当前配置
    show_current_config()
    
    print("\n🔍 检查API密钥配置:")
    
    # 验证API密钥
    if validate_api_keys():
        print("\n🎉 所有API密钥配置完成！")
        print("现在可以运行TradingAgents项目了:")
        print("  python -m cli.main")
        print("  或")
        print("  python main.py")
    else:
        show_api_info()
        sys.exit(1)

if __name__ == "__main__":
    main()
