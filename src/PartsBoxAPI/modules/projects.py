from typing import Optional
from .base import BaseAPI

class ProjectsAPI(BaseAPI):
    """
    API module for managing projects.
    """
    def get_project(self, project_id: str) -> dict:
        """
        Retrieve details of a specific project.

        :param project_id: The ID of the project to retrieve.
        :return: A dictionary containing project details.
        """
        response = self._send_request("/project/get", project_id=project_id)
        return response

    def get_all_projects(self) -> list:
        """
        Retrieve a list of all projects.

        :return: A list of all projects.
        """
        response = self._send_request("/project/all")
        return response

    def create_project(self, project_name: str, project_description: Optional[str] = None, project_notes: Optional[str] = None, project_tags: Optional[list] = None) -> dict:
        """
        Create a new project.

        :param project_name: The name of the project.
        :param project_description: Optional description of the project.
        :param project_notes: Optional notes for the project.
        :param project_tags: Optional tags for the project.
        :return: A dictionary containing the newly created project's details.
        """
        response = self._send_request("/project/create", project_name=project_name, project_description=project_description, project_notes=project_notes, project_tags=project_tags)
        return response

    def update_project(self, project_id: str, project_name: Optional[str] = None, project_description: Optional[str] = None, project_notes: Optional[str] = None, project_tags: Optional[list] = None) -> dict:
        """
        Update details of an existing project.

        :param project_id: The ID of the project to update.
        :param project_name: Optional new name for the project.
        :param project_description: Optional new description for the project.
        :param project_notes: Optional new notes for the project.
        :param project_tags: Optional new tags for the project.
        :return: A dictionary containing the updated project's details.
        """
        response = self._send_request("/project/update", project_id=project_id, project_name=project_name, project_description=project_description, project_notes=project_notes, project_tags=project_tags)
        return response

    def delete_project(self, project_id: str) -> dict:
        """
        Delete a specific project.

        :param project_id: The ID of the project to delete.
        :return: A dictionary containing the status of the deletion.
        """
        response = self._send_request("/project/delete", project_id=project_id)
        return response

    def get_project_entries(self, project_id: str) -> list:
        """
        Retrieve a list of entries for a specific project.

        :param project_id: The ID of the project.
        :return: A list of entries for the project.
        """
        response = self._send_request("/project/get-entries", project_id=project_id)
        return response

    def add_project_entries(self, project_id: str, entries: list) -> dict:
        """
        Add entries to a specific project.

        :param project_id: The ID of the project.
        :param entries: A list of entries to add.
        :return: A dictionary containing the status of the operation.
        """
        response = self._send_request("/project/add-entries", project_id=project_id, entries=entries)
        return response

    def update_project_entries(self, project_id: str, entries: list) -> dict:
        """
        Update entries for a specific project.

        :param project_id: The ID of the project.
        :param entries: A list of entries to update.
        :return: A dictionary containing the status of the operation.
        """
        response = self._send_request("/project/update-entries", project_id=project_id, entries=entries)
        return response

    def delete_project_entries(self, project_id: str, ids: list) -> dict:
        """
        Delete entries from a specific project.

        :param project_id: The ID of the project.
        :param entry_ids: A list of entry IDs to delete.
        :return: A dictionary containing the status of the operation.
        """
        response = self._send_request("/project/delete-entries", project_id=project_id, ids=ids)
        return response

    def get_project_builds(self, project_id: str) -> list:
        """
        Retrieve a list of builds for a specific project.

        :param project_id: The ID of the project.
        :return: A list of builds for the project.
        """
        response = self._send_request("/project/get-builds", project_id=project_id)
        return response

    def archive_project(self, project_id: str) -> dict:
        """
        Archive a specific project.

        :param project_id: The ID of the project to archive.
        :return: A dictionary containing the status of the archive operation.
        """
        response = self._send_request("/project/archive", project_id=project_id)
        return response

    def restore_project(self, project_id: str) -> dict:
        """
        Restore a specific archived project.

        :param project_id: The ID of the project to restore.
        :return: A dictionary containing the status of the restore operation.
        """
        response = self._send_request("/project/restore", project_id=project_id)
        return response