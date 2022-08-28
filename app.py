import requests

from app_logger import logger

url = 'http://www.google.co.in'

logger.info(f"Request for {url} going to start")

status = requests.get('http://www.google.co.in')

logger.info(f"Response status code {status.status_code}")

logger.debug(status.text)

logger.info("Completed...")
