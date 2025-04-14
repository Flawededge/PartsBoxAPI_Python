import requests
from loguru import logger
from typing import Any
import threading
import time

class BaseAPI:
    """
    Base class for PartsBox API modules.
    """
    BASE_URL = "https://api.partsbox.com/api/1"
    RATE_LIMIT = 5  # Maximum number of requests per second
    _lock = threading.Lock()
    _last_request_time = 0

    def __init__(self, session: requests.Session):
        self.session = session

    def _send_request(self, endpoint: str, **kwargs) -> Any:
        """
        Send a POST request to the PartsBox API with rate limiting.

        :param endpoint: API endpoint (e.g., "/part/get").
        :param kwargs: Parameters to include in the request body.
        :return: Parsed JSON response.
        """
        url = f"{self.BASE_URL}{endpoint}"

        # Enforce rate limiting
        with self._lock:
            current_time = time.time()
            elapsed_time = current_time - self._last_request_time
            if elapsed_time < 1 / self.RATE_LIMIT:
                time.sleep((1 / self.RATE_LIMIT) - elapsed_time)
            self._last_request_time = time.time()

        logger.info(f"Sending request to {url} with payload: {kwargs}")
        response = self.session.post(url, json=kwargs)
        response.raise_for_status()
        return response.json()
