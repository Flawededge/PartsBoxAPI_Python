from typing import Optional, Any
from .base import BaseAPI

class StorageAPI(BaseAPI):
    """
    API module for managing storage.
    """
    def get_storage(self, storage_id: str) -> dict:
        """
        Retrieve details of a specific storage location.

        :param storage_id: The ID of the storage location to retrieve.
        :return: A dictionary containing storage details.
        """
        response = self._send_request("/storage/get", storage_id=storage_id)
        return response

    def get_all_storage(self) -> list:
        """
        Retrieve a list of all storage locations.

        :return: A list of all storage locations.
        """
        response = self._send_request("/storage/all")
        return response

    def update_storage(self, storage_id: str, storage_name: Optional[str] = None, storage_description: Optional[str] = None, storage_tags: Optional[list] = None) -> dict:
        """
        Update details of a specific storage location.

        :param storage_id: The ID of the storage location to update.
        :param storage_name: Optional new name for the storage location.
        :param storage_description: Optional new description for the storage location.
        :param storage_tags: Optional new tags for the storage location.
        :return: A dictionary containing the status of the update.
        """
        response = self._send_request("/storage/update", storage_id=storage_id, storage_name=storage_name, storage_description=storage_description, storage_tags=storage_tags)
        return response

    def rename_storage(self, storage_id: str, new_name: str) -> dict:
        """
        Rename a specific storage location.

        :param storage_id: The ID of the storage location to rename.
        :param new_name: The new name for the storage location.
        :return: A dictionary containing the status of the rename operation.
        """
        response = self._send_request("/storage/rename", storage_id=storage_id, new_name=new_name)
        return response

    def change_storage_settings(self, storage_id: str, setting_key: str, setting_value: Any) -> dict:
        """
        Change settings for a specific storage location.

        :param storage_id: The ID of the storage location.
        :param setting_key: The key of the setting to change.
        :param setting_value: The new value for the setting.
        :return: A dictionary containing the status of the operation.
        """
        response = self._send_request("/storage/change-settings", storage_id=storage_id, setting_key=setting_key, setting_value=setting_value)
        return response

    def archive_storage(self, storage_id: str) -> dict:
        """
        Archive a specific storage location.

        :param storage_id: The ID of the storage location to archive.
        :return: A dictionary containing the status of the archive operation.
        """
        response = self._send_request("/storage/archive", storage_id=storage_id)
        return response

    def restore_storage(self, storage_id: str) -> dict:
        """
        Restore a specific archived storage location.

        :param storage_id: The ID of the storage location to restore.
        :return: A dictionary containing the status of the restore operation.
        """
        response = self._send_request("/storage/restore", storage_id=storage_id)
        return response

    def get_storage_parts(self, storage_id: str) -> list:
        """
        Retrieve a list of parts in a specific storage location.

        :param storage_id: The ID of the storage location.
        :return: A list of parts in the storage location.
        """
        response = self._send_request("/storage/parts", storage_id=storage_id)
        return response

    def get_storage_lots(self, storage_id: str) -> list:
        """
        Retrieve a list of lots in a specific storage location.

        :param storage_id: The ID of the storage location.
        :return: A list of lots in the storage location.
        """
        response = self._send_request("/storage/lots", storage_id=storage_id)
        return response