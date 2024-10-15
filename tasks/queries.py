from typing import TypedDict
from tasks.models import InternalProject, ExternalProject
from django.db.models import TextChoices


def get_internal_projects_total_cost() -> float:
    """
    TODO: Implement this function to return the total cost of internal projects.

    Total cost of an internal project is the sum of `project.production_cost` and`project.maintanance_cost` field values.
    """
    return 0.0


class ProjectType(TextChoices):
    INTERNAL = "internal", "Internal"
    EXTERNAL = "external", "External"


class ProjectData(TypedDict):
    id: int
    name: str
    type: ProjectType


def get_all_projects() -> list[ProjectData]:
    """
    TODO: Implement this function to return a combined list of projects sorted by name.

    Example output:
        [
            {"id": 1, "name": "Project Alpha", "type": "internal"},
            {"id": 2, "name": "Project Beta", "type": "external"}
        ]
    """
    return []
