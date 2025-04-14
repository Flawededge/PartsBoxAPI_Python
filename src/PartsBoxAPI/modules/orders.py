from typing import Optional
from .base import BaseAPI

class OrdersAPI(BaseAPI):
    """
    API module for managing orders.
    """
    def get_order(self, order_id: str) -> dict:
        """
        Retrieve details of a specific order.

        :param order_id: The ID of the order to retrieve.
        :return: A dictionary containing order details.
        """
        response = self._send_request("/order/get", order_id=order_id)
        return response

    def get_all_orders(self) -> list:
        """
        Retrieve a list of all orders.

        :return: A list of all orders.
        """
        response = self._send_request("/order/all")
        return response

    def get_order_entries(self, order_id: str) -> list:
        """
        Retrieve entries for a specific order.

        :param order_id: The ID of the order.
        :return: A list of entries for the order.
        """
        response = self._send_request("/order/get-entries", order_id=order_id)
        return response

    def receive_order(self, order_id: str, entries: list) -> dict:
        """
        Mark entries in an order as received.

        :param order_id: The ID of the order.
        :param entries: A list of entries to mark as received.
        :return: A dictionary containing the status of the operation.
        """
        response = self._send_request("/order/receive", order_id=order_id, entries=entries)
        return response