import os

from dotenv import load_dotenv

from utils.Logger import logger

load_dotenv()


def is_true(stream):
    if isinstance(stream, str):
        return stream.lower() in ['true', '1', 't', 'y', 'yes']
    elif isinstance(stream, int):
        return stream == 1
    else:
        return False


authorization = os.getenv('AUTHORIZATION', '').replace(' ', '')
chatgpt_base_url = os.getenv('CHATGPT_BASE_URL', 'https://chat.openai.com').replace(' ', '')
arkose_token_url = os.getenv('ARKOSE_TOKEN_URL', '').replace(' ', '')
proxy_url = os.getenv('PROXY_URL', '').replace(' ', '')
history_disabled_str = os.getenv('HISTORY_DISABLED', 'true').replace(' ', '')
history_disabled = is_true(history_disabled_str)
retry_times = int(os.getenv('RETRY_TIMES', 3))

authorization_list = authorization.split(',') if authorization else []
chatgpt_base_url_list = chatgpt_base_url.split(',') if chatgpt_base_url else []
arkose_token_url_list = arkose_token_url.split(',') if arkose_token_url else []
proxy_url_list = proxy_url.split(',') if proxy_url else []

logger.info("Environment variables (no AUTHORIZATION):")
logger.info("CHATGPT_BASE_URL:      " + str(chatgpt_base_url_list))
logger.info("ARKOSE_TOKEN_URL:      " + str(arkose_token_url_list))
logger.info("PROXY_URL:             " + str(proxy_url_list))
logger.info("HISTORY_DISABLED:      " + str(history_disabled))
logger.info("RETRY_TIMES:           " + str(retry_times))
