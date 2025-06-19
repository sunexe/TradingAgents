# Yahoo Finance API 限制解决方案

## 问题描述
Yahoo Finance API 存在请求频率限制，当请求过于频繁时会返回错误："Yahoo Finance API is still rate-limited"。

## 解决方案

### 1. 自动重试机制
项目已经实现了智能重试机制：
- 最多重试3次
- 指数退避延迟（5秒、10秒、20秒）
- 添加随机抖动避免同步请求

### 2. 数据源优先级
系统会按以下优先级获取数据：
1. **本地缓存数据**（最快，无限制）
2. **Yahoo Finance在线API**（有限制，但数据最新）
3. **Finnhub API**（备用数据源）
4. **其他替代API**

### 3. 智能数据获取函数
使用新的 `get_stock_data_smart()` 函数：
```python
# 自动选择最佳数据源
data = get_stock_data_smart("TSLA", "2024-01-01", "2024-12-31")
```

### 4. 配置选项
在 `data_source_config.py` 中可以调整：
- 重试次数和延迟时间
- 数据源优先级
- 速率限制参数

## 使用建议

### 避免速率限制：
1. **使用本地数据**：如果日期范围在2015-2025年之间，优先使用本地缓存
2. **合理间隔**：连续请求之间等待5-10秒
3. **批量处理**：一次性获取较长时间范围的数据，而不是多次短期请求
4. **错峰请求**：避免在美股交易时间内高频请求

### 替代方案：
1. **使用Finnhub API**：
   - 注册免费账户获取API密钥
   - 每天6万次免费请求
   - 设置环境变量：`FINNHUB_API_KEY=your_key`

2. **使用Alpha Vantage API**：
   - 免费版每天500次请求
   - 更稳定的服务

3. **下载历史数据**：
   - 手动下载CSV文件到 `data/market_data/price_data/` 目录
   - 文件格式：`{SYMBOL}-YFin-data-{start_date}-{end_date}.csv`

## 监控和调试

### 检查数据源状态：
```bash
python3 -c "
from tradingagents.dataflows.interface import get_stock_data_smart
print(get_stock_data_smart('AAPL', '2024-01-01', '2024-01-31'))
"
```

### 查看错误日志：
系统会显示详细的错误信息和重试过程，帮助诊断问题。

### 测试API连接：
```bash
python3 -c "
import yfinance as yf
ticker = yf.Ticker('AAPL')
print('API连接正常' if ticker.info else 'API连接异常')
"
```

## 长期解决方案

1. **设置数据缓存系统**：定期更新本地数据
2. **使用付费API服务**：获得更高的请求限制
3. **实现数据代理**：通过代理服务器分散请求
4. **使用WebSocket实时数据**：减少REST API调用

## 注意事项

- Yahoo Finance API的限制可能会随时变化
- 建议在生产环境中使用付费的金融数据服务
- 遵守API服务条款，避免滥用
- 考虑数据延迟对交易决策的影响
