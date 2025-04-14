from typing import Optional
from .base import BaseAPI

class PartsAPI(BaseAPI):
    """
    API module for managing parts.
    """
    def get_all_parts(self) -> list:
        """
        Retrieve all parts from the PartsBox API.

        :return: A list of all parts.
        """
        response = self._send_request("/part/all")
        return response

    def get_part(self, part_id: str) -> dict:
        """
        Retrieve a specific part by its ID.

        :param part_id: The ID of the part to retrieve.
        :return: A dictionary containing part details.
        """
        response = self._send_request("/part/get", part_id=part_id)
        return response

    def create_part(self, part_type: str, part_name: str, part_description: Optional[str] = None, part_notes: Optional[str] = None, part_tags: Optional[list] = None, part_footprint: Optional[str] = None, part_attrition: Optional[dict] = None, part_low_stock: Optional[dict] = None) -> dict:
        """
        Create a new part in the PartsBox system.

        :param part_type: The type of the part "sub-assembly", "meta", "linked", "local".
        :param part_name: The name of the part.
        :param part_description: Optional description of the part.
        :param part_notes: Optional notes for the part.
        :param part_tags: Optional tags associated with the part.
        :param part_footprint: Optional footprint of the part.
        :param part_attrition: Optional attrition details for the part.
        :param part_low_stock: Optional low stock threshold for the part.
        :return: A dictionary containing the newly created part's details.
        """
        response = self._send_request("/part/create", part_type=part_type, part_name=part_name, part_description=part_description, part_notes=part_notes, part_tags=part_tags, part_footprint=part_footprint, part_attrition=part_attrition, part_low_stock=part_low_stock)
        return response

    def update_part(self, part_id: str, part_name: Optional[str] = None, part_description: Optional[str] = None, part_notes: Optional[str] = None, part_tags: Optional[list] = None, part_footprint: Optional[str] = None, part_attrition: Optional[dict] = None, part_low_stock: Optional[dict] = None) -> dict:
        """
        Update details of an existing part.

        :param part_id: The ID of the part to update.
        :param part_name: Optional new name for the part.
        :param part_description: Optional new description for the part.
        :param part_notes: Optional new notes for the part.
        :param part_tags: Optional new tags for the part.
        :param part_footprint: Optional new footprint for the part.
        :param part_attrition: Optional new attrition details for the part.
        :param part_low_stock: Optional new low stock threshold for the part.
        :return: A dictionary containing the updated part's details.
        """
        response = self._send_request("/part/update", part_id=part_id, part_name=part_name, part_description=part_description, part_notes=part_notes, part_tags=part_tags, part_footprint=part_footprint, part_attrition=part_attrition, part_low_stock=part_low_stock)
        return response

    def delete_part(self, part_id: str) -> dict:
        """
        Delete a part from the PartsBox system.

        :param part_id: The ID of the part to delete.
        :return: A dictionary containing the status of the deletion.
        """
        response = self._send_request("/part/delete", part_id=part_id)
        return response

    def add_meta_part_ids(self, part_id: str, meta_part_ids: list) -> dict:
        """
        Add meta part IDs to a part.

        :param part_id: The ID of the part.
        :param meta_part_ids: A list of meta part IDs to add.
        :return: A dictionary containing the status of the operation.
        """
        response = self._send_request("/part/add-meta-part-ids", part_id=part_id, meta_part_ids=meta_part_ids)
        return response

    def remove_meta_part_ids(self, part_id: str, meta_part_ids: list) -> dict:
        """
        Remove meta part IDs from a part.

        :param part_id: The ID of the part.
        :param meta_part_ids: A list of meta part IDs to remove.
        :return: A dictionary containing the status of the operation.
        """
        response = self._send_request("/part/remove-meta-part-ids", part_id=part_id, meta_part_ids=meta_part_ids)
        return response

    def add_substitute_ids(self, part_id: str, substitute_ids: list) -> dict:
        """
        Add substitute part IDs to a part.

        :param part_id: The ID of the part.
        :param substitute_ids: A list of substitute part IDs to add.
        :return: A dictionary containing the status of the operation.
        """
        response = self._send_request("/part/add-substitute-ids", part_id=part_id, substitute_ids=substitute_ids)
        return response

    def remove_substitute_ids(self, part_id: str, substitute_ids: list) -> dict:
        """
        Remove substitute part IDs from a part.

        :param part_id: The ID of the part.
        :param substitute_ids: A list of substitute part IDs to remove.
        :return: A dictionary containing the status of the operation.
        """
        response = self._send_request("/part/remove-substitute-ids", part_id=part_id, substitute_ids=substitute_ids)
        return response

    def update_custom_fields(self, part_id: str, custom_fields: dict) -> dict:
        """
        Update custom fields for a part.

        :param part_id: The ID of the part.
        :param custom_fields: A dictionary of custom fields to update.
        :return: A dictionary containing the status of the operation.
        """
        response = self._send_request("/part/update-custom-fields", part_id=part_id, custom_fields=custom_fields)
        return response

    def delete_custom_field(self, part_id: str, field_name: str) -> dict:
        """
        Delete a custom field from a part.

        :param part_id: The ID of the part.
        :param field_name: The name of the custom field to delete.
        :return: A dictionary containing the status of the operation.
        """
        response = self._send_request("/part/delete-custom-field", part_id=part_id, field_name=field_name)
        return response

    def get_storage_info(self, part_id: str) -> dict:
        """
        Retrieve storage information for a part.

        :param part_id: The ID of the part.
        :return: A dictionary containing storage information for the part.
        """
        response = self._send_request("/part/storage", part_id=part_id)
        return response

    def get_lot_info(self, part_id: str) -> dict:
        """
        Retrieve lot information for a part.

        :param part_id: The ID of the part.
        :return: A dictionary containing lot information for the part.
        """
        response = self._send_request("/part/lots", part_id=part_id)
        return response

    def get_stock_info(self, part_id: str) -> dict:
        """
        Retrieve stock information for a part.

        :param part_id: The ID of the part.
        :return: A dictionary containing stock information for the part.
        """
        response = self._send_request("/part/stock", part_id=part_id)
        return response