from typing import Optional
from .base import BaseAPI

class OffersAPI(BaseAPI):
    """
    API module for managing offers.
    """
    def get_offer(self, offer_id: str) -> dict:
        """
        Retrieve details of a specific offer.

        :param offer_id: The ID of the offer to retrieve.
        :return: A dictionary containing offer details.
        """
        response = self._send_request("/offer/get", offer_id=offer_id)
        return response

    def get_all_offers(self) -> list:
        """
        Retrieve a list of all offers.

        :return: A list of all offers.
        """
        response = self._send_request("/offer/all")
        return response