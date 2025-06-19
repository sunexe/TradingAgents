# 创建一个使用DeepSeek API的示例配置文件
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# 加载.env文件中的环境变量
load_dotenv()

# 验证必需的环境变量
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("请在.env文件中设置OPENAI_API_KEY（DeepSeek API密钥）")
if not os.getenv("FINNHUB_API_KEY"):
    raise ValueError("请在.env文件中设置FINNHUB_API_KEY")

print(f"✅ 使用API端点: {os.getenv('OPENAI_BASE_URL', 'https://api.openai.com/v1')}")
print(f"✅ API密钥已加载: {os.getenv('OPENAI_API_KEY')[:8]}...")
print(f"✅ FINNHUB密钥已加载: {os.getenv('FINNHUB_API_KEY')[:8]}...")

# 创建自定义配置
config = DEFAULT_CONFIG.copy()
config["deep_think_llm"] = "deepseek-chat"      # 使用DeepSeek模型
config["quick_think_llm"] = "deepseek-chat"     # 使用DeepSeek模型
config["max_debate_rounds"] = 1
config["online_tools"] = True

# 自定义TradingAgentsGraph类以支持DeepSeek
class DeepSeekTradingAgentsGraph(TradingAgentsGraph):
    def __init__(self, selected_analysts=None, debug=False, config=None):
        # 如果没有指定分析师，使用默认的分析师列表
        if selected_analysts is None:
            selected_analysts = ["market", "social", "news", "fundamentals"]
        
        # 调用父类初始化
        super().__init__(selected_analysts, debug, config)
        
        # 重新初始化LLMs以使用DeepSeek API
        self.deep_thinking_llm = ChatOpenAI(
            model=self.config["deep_think_llm"],
            base_url="https://api.deepseek.com",
            api_key=os.getenv("DEEPSEEK_API_KEY", os.getenv("OPENAI_API_KEY"))
        )
        self.quick_thinking_llm = ChatOpenAI(
            model=self.config["quick_think_llm"],
            base_url="https://api.deepseek.com",
            api_key=os.getenv("DEEPSEEK_API_KEY", os.getenv("OPENAI_API_KEY")),
            temperature=0.1
        )

# 使用示例
if __name__ == "__main__":
    # 初始化DeepSeek版本的TradingAgents
    ta = DeepSeekTradingAgentsGraph(debug=True, config=config)
    
    # 运行分析
    _, decision = ta.propagate("NVDA", "2024-05-10")
    print(decision)
