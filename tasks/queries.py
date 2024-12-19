from typing import TypedDict

from django.db.models import TextChoices

from tasks.models import ExternalProject, InternalProject


def get_average_internal_project_cost() -> float:
    """
    TODO: Implement this function to return the average cost of internal projects.

    Internal project cost is a sum of production cost and maintenance cost.
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
