import os
from typing import Optional
import requests
from dotenv import load_dotenv

from .modules.base import BaseAPI
from .modules.parts import PartsAPI
from .modules.stock import StockAPI
from .modules.lots import LotsAPI
from .modules.storage import StorageAPI
from .modules.projects import ProjectsAPI
from .modules.orders import OrdersAPI
from .modules.offers import OffersAPI
from .modules.purchase_lists import PurchaseListsAPI
from .modules.id_anything import IDAnythingAPI
from .modules.global_api import GlobalAPI
# Load environment variables from a .env file (if present)
load_dotenv()

# Import all of the API modules

class PartsBoxAPI:
    """
    Main API client that combines all individual API modules.
    """
    BASE_URL = "https://api.partsbox.com/api/1"
    RATE_LIMIT = 5  # Default global rate limit (requests per second)

    def __init__(self, api_key: Optional[str] = None):
        # Set the global rate limit for BaseAPI
        BaseAPI.RATE_LIMIT = self.RATE_LIMIT

        self.api_key = api_key
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({"Authorization": f"APIKey {api_key}"})
        else:
            self.api_key = os.getenv("PARTSBOX_API_KEY")
            if not self.api_key:
                raise ValueError("API key must be provided or set in the environment variable 'PARTSBOX_API_KEY'.")
        
        # Initialize all API modules
        self.parts = PartsAPI(self.session)
        self.stock = StockAPI(self.session)
        self.lots = LotsAPI(self.session)
        self.storage = StorageAPI(self.session)
        self.projects = ProjectsAPI(self.session)
        self.orders = OrdersAPI(self.session)
        self.offers = OffersAPI(self.session)
        self.purchase_lists = PurchaseListsAPI(self.session)
        self.id_anything = IDAnythingAPI(self.session)
        self.global_api = GlobalAPI(self.session)
    
    @classmethod
    def set_global_rate_limit(cls, rate_limit: int):
        """
        Set the global rate limit for all API modules.

        :param rate_limit: Rate limit in requests per second.
        """
        BaseAPI.RATE_LIMIT = rate_limit