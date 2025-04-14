from .base import BaseAPI

class IDAnythingAPI(BaseAPI):
    """
    API module for managing ID Anything™ functionality.
    """
    def get_id_anything_qr(self, id_anything_id: str) -> bytes:
        """
        Retrieve the QR code for a specific ID Anything™.

        :param id_anything_id: The ID of the ID Anything™ to retrieve the QR code for.
        :return: The QR code image as bytes.
        """
        response = self._send_request("/id-anything-qr", id_anything_id=id_anything_id)
        return response.content