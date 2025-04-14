from typing import Optional, Dict
from .base import BaseAPI

class LotsAPI(BaseAPI):
    """
    API module for managing lots.
    """
    def get_lot(self, lot_id: str) -> dict:
        """
        Retrieve details of a specific lot.

        :param lot_id: The ID of the lot to retrieve.
        :return: A dictionary containing lot details.
        """
        response = self._send_request("/lot/get", lot_id=lot_id)
        return response

    def update_lot(self, lot_id: str, lot_notes: Optional[str] = None, lot_tags: Optional[list] = None) -> dict:
        """
        Update details of a specific lot.

        :param lot_id: The ID of the lot to update.
        :param lot_notes: Optional notes for the lot.
        :param lot_tags: Optional tags for the lot.
        :return: A dictionary containing the status of the update.
        """
        response = self._send_request("/lot/update", lot_id=lot_id, lot_notes=lot_notes, lot_tags=lot_tags)
        return response

    def get_all_lots(self) -> list:
        """
        Retrieve a list of all lots.

        :return: A list of all lots.
        """
        response = self._send_request("/lot/all")
        return response