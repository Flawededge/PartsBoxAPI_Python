from typing import Optional
from .base import BaseAPI

class GlobalAPI(BaseAPI):
    """
    API module for global actions.
    """
    def download_all_data(self) -> bytes:
        """
        Download all data from the PartsBox system.

        :return: The data as bytes.
        """
        response = self._send_request("/db/download-all-data")
        return response.content