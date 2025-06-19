# Data Source Configuration
# This file manages data source priorities and retry settings for TradingAgents

# Yahoo Finance API Settings
YFINANCE_CONFIG = {
    "max_retries": 3,
    "base_delay": 5,  # seconds
    "max_delay": 30,  # seconds
    "random_jitter": True,
    "enable_cache_fallback": True
}

# Data Source Priority (1 = highest priority)
DATA_SOURCE_PRIORITY = {
    "local_cache": 1,
    "yahoo_finance": 2,
    "finnhub": 3,
    "alternative_apis": 4
}

# Rate Limiting Configuration
RATE_LIMITING = {
    "yahoo_finance": {
        "requests_per_minute": 60,
        "requests_per_hour": 2000,
        "cooldown_period": 300  # seconds to wait after rate limit
    },
    "finnhub": {
        "requests_per_minute": 60,
        "requests_per_second": 1
    }
}

# Fallback behavior
FALLBACK_CONFIG = {
    "use_cached_data_on_failure": True,
    "max_cache_age_days": 30,
    "show_data_source_info": True
}

# Error handling
ERROR_HANDLING = {
    "retry_on_connection_error": True,
    "retry_on_timeout": True,
    "retry_on_rate_limit": True,
    "log_errors": True
}
