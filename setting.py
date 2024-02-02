import logging.config
import json
import os


# 定义日志配置字典
log_json_path = './config/logger.json'
with open(log_json_path, 'r', encoding='utf-8') as load_f:
    log_config = json.load(load_f)

# 参数 exist_ok=True 表示如果目录已经存在，不会引发错误，而是跳过创建操作
os.makedirs('logs', exist_ok=True)

# 配置日志记录器
logging.config.dictConfig(log_config)

# 示例日志输出
logger = logging.getLogger(__name__)

# 使用样例
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')