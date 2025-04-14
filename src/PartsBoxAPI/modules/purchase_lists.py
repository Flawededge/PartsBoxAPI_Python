from typing import Optional
from .base import BaseAPI

class PurchaseListsAPI(BaseAPI):
    """
    API module for managing purchase lists.
    """
    def create_list(self, list_name: str, entries: list) -> dict:
        """
        Create a new purchase list.

        :param list_name: The name of the purchase list.
        :param entries: A list of entries to include in the purchase list.
        :return: A dictionary containing the status of the operation.
        """
        response = self._send_request("/list/create", list_name=list_name, entries=entries)
        return response

    def add_entries_to_list(self, list_id: str, entries: list) -> dict:
        """
        Add entries to an existing purchase list.

        :param list_id: The ID of the purchase list.
        :param entries: A list of entries to add.
        :return: A dictionary containing the status of the operation.
        """
        response = self._send_request("/list/add-entries", list_id=list_id, entries=entries)
        return response

    def get_list(self, list_id: str) -> dict:
        """
        Retrieve details of a specific purchase list.

        :param list_id: The ID of the purchase list to retrieve.
        :return: A dictionary containing purchase list details.
        """
        response = self._send_request("/list/get", list_id=list_id)
        return response

    def get_list_entries(self, list_id: str) -> list:
        """
        Retrieve entries for a specific purchase list.

        :param list_id: The ID of the purchase list.
        :return: A list of entries in the purchase list.
        """
        response = self._send_request("/list/get-entries", list_id=list_id)
        return response

    def delete_list(self, list_id: str) -> dict:
        """
        Delete a specific purchase list.

        :param list_id: The ID of the purchase list to delete.
        :return: A dictionary containing the status of the deletion.
        """
        response = self._send_request("/list/delete", list_id=list_id)
        return response