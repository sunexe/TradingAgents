#!/usr/bin/env python3
"""
数据下载和缓存脚本
用于下载股票数据并保存到本地，避免频繁调用API
"""

import os
import sys
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import time
import random

# 添加项目路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tradingagents.dataflows.config import get_config

def download_stock_data(symbol, start_date="2020-01-01", end_date=None):
    """下载股票数据并保存到本地缓存"""
    if end_date is None:
        end_date = datetime.now().strftime("%Y-%m-%d")
    
    config = get_config()
    data_dir = config["data_dir"]
    
    print(f"下载 {symbol} 的数据从 {start_date} 到 {end_date}...")
    
    try:
        # 添加随机延迟避免速率限制
        time.sleep(random.uniform(1, 3))
        
        ticker = yf.Ticker(symbol)
        data = ticker.history(start=start_date, end=end_date)
        
        if data.empty:
            print(f"⚠ {symbol} 没有找到数据")
            return False
        
        # 重置索引，使Date成为一列
        data.reset_index(inplace=True)
        
        # 确保目录存在
        price_data_dir = os.path.join(data_dir, "market_data", "price_data")
        os.makedirs(price_data_dir, exist_ok=True)
        
        # 保存数据
        filename = f"{symbol}-YFin-data-{start_date}-{end_date}.csv"
        filepath = os.path.join(price_data_dir, filename)
        data.to_csv(filepath, index=False)
        
        print(f"✓ {symbol} 数据已保存到 {filepath}")
        print(f"  数据范围: {data['Date'].min()} 到 {data['Date'].max()}")
        print(f"  数据点数: {len(data)} 条")
        
        return True
        
    except Exception as e:
        print(f"✗ 下载 {symbol} 数据失败: {e}")
        return False

def download_popular_stocks():
    """下载一些热门股票的数据"""
    popular_stocks = [
        "AAPL",  # Apple
        "TSLA",  # Tesla
        "GOOGL", # Google
        "MSFT",  # Microsoft
        "AMZN",  # Amazon
        "NVDA",  # Nvidia
        "META",  # Meta
        "SPY",   # S&P 500 ETF
    ]
    
    successful_downloads = 0
    
    for symbol in popular_stocks:
        if download_stock_data(symbol):
            successful_downloads += 1
        
        # 添加延迟避免速率限制
        time.sleep(random.uniform(3, 7))
    
    print(f"\n完成! 成功下载 {successful_downloads}/{len(popular_stocks)} 只股票的数据")

def create_sample_data():
    """创建一些示例数据用于测试"""
    config = get_config()
    data_dir = config["data_dir"]
    
    # 创建示例TSLA数据
    dates = pd.date_range(start="2024-01-01", end="2024-06-19", freq="D")
    dates = [d for d in dates if d.weekday() < 5]  # 只保留工作日
    
    # 生成模拟TSLA价格数据
    base_price = 200
    prices = []
    current_price = base_price
    
    for i, date in enumerate(dates):
        # 简单的随机游走模型
        change = random.uniform(-0.05, 0.05)  # -5% 到 +5% 的日变化
        current_price *= (1 + change)
        
        # 确保价格在合理范围内
        current_price = max(50, min(400, current_price))
        
        prices.append({
            "Date": date.strftime("%Y-%m-%d"),
            "Open": round(current_price * random.uniform(0.98, 1.02), 2),
            "High": round(current_price * random.uniform(1.00, 1.05), 2),
            "Low": round(current_price * random.uniform(0.95, 1.00), 2),
            "Close": round(current_price, 2),
            "Adj Close": round(current_price, 2),
            "Volume": random.randint(10000000, 100000000)
        })
    
    # 保存示例数据
    sample_df = pd.DataFrame(prices)
    price_data_dir = os.path.join(data_dir, "market_data", "price_data")
    os.makedirs(price_data_dir, exist_ok=True)
    
    sample_filepath = os.path.join(price_data_dir, "TSLA-YFin-data-2024-01-01-2024-06-19.csv")
    sample_df.to_csv(sample_filepath, index=False)
    
    print(f"✓ 创建示例TSLA数据: {sample_filepath}")
    print(f"  数据范围: 2024-01-01 到 2024-06-19")
    print(f"  数据点数: {len(sample_df)} 条")

if __name__ == "__main__":
    print("TradingAgents 数据下载脚本")
    print("=" * 50)
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "sample":
            print("创建示例数据...")
            create_sample_data()
        elif sys.argv[1] == "download":
            print("下载真实市场数据...")
            download_popular_stocks()
        else:
            symbol = sys.argv[1].upper()
            print(f"下载 {symbol} 数据...")
            download_stock_data(symbol)
    else:
        print("使用方法:")
        print("  python3 download_data.py sample       # 创建示例数据")
        print("  python3 download_data.py download     # 下载热门股票数据")
        print("  python3 download_data.py TSLA         # 下载特定股票数据")
        print()
        print("创建示例数据以便快速测试...")
        create_sample_data()
