from typing import Optional
from .base import BaseAPI

class StockAPI(BaseAPI):
    """
    API module for managing stock.
    """
    def add_stock(self, part_id: str, quantity: int, storage_id: Optional[str] = None, lot_id: Optional[str] = None, notes: Optional[str] = None) -> dict:
        """
        Add stock for a specific part.

        :param part_id: The ID of the part.
        :param quantity: The quantity to add.
        :param storage_id: Optional storage location ID.
        :param lot_id: Optional lot ID.
        :param notes: Optional notes for the stock addition.
        :return: A dictionary containing the status of the operation.
        """
        response = self._send_request("/stock/add", part_id=part_id, quantity=quantity, storage_id=storage_id, lot_id=lot_id, notes=notes)
        return response

    def remove_stock(self, part_id: str, quantity: int, storage_id: Optional[str] = None, lot_id: Optional[str] = None, notes: Optional[str] = None) -> dict:
        """
        Remove stock for a specific part.

        :param part_id: The ID of the part.
        :param quantity: The quantity to remove.
        :param storage_id: Optional storage location ID.
        :param lot_id: Optional lot ID.
        :param notes: Optional notes for the stock removal.
        :return: A dictionary containing the status of the operation.
        """
        response = self._send_request("/stock/remove", part_id=part_id, quantity=quantity, storage_id=storage_id, lot_id=lot_id, notes=notes)
        return response

    def move_stock(self, part_id: str, from_storage: str, to_storage: str, quantity: int, lot_id: Optional[str] = None, notes: Optional[str] = None) -> dict:
        """
        Move stock from one storage location to another.

        :param part_id: The ID of the part.
        :param from_storage: The ID of the source storage location.
        :param to_storage: The ID of the destination storage location.
        :param quantity: The quantity to move.
        :param lot_id: Optional lot ID.
        :param notes: Optional notes for the stock movement.
        :return: A dictionary containing the status of the operation.
        """
        response = self._send_request("/stock/move", part_id=part_id, from_storage=from_storage, to_storage=to_storage, quantity=quantity, lot_id=lot_id, notes=notes)
        return response

    def update_stock(self, part_id: str, quantity: Optional[int] = None, storage_id: Optional[str] = None, lot_id: Optional[str] = None, notes: Optional[str] = None) -> dict:
        """
        Update stock details for a specific part.

        :param part_id: The ID of the part.
        :param quantity: Optional new quantity.
        :param storage_id: Optional storage location ID.
        :param lot_id: Optional lot ID.
        :param notes: Optional notes for the stock update.
        :return: A dictionary containing the status of the operation.
        """
        response = self._send_request("/stock/update", part_id=part_id, quantity=quantity, storage_id=storage_id, lot_id=lot_id, notes=notes)
        return response