from tasks.models import ExternalProject, InternalProject, InternalProjectTask


def internal_project_factory(
    *,
    name: str,
    production_cost: float = 0,
    maintanance_cost: float = 0,
) -> InternalProject:
    return InternalProject.objects.create(
        name=name, production_cost=production_cost, maintanance_cost=maintanance_cost
    )


def external_project_factory(
    *,
    name: str,
    client_name: str,
    deleted: bool = False,
) -> ExternalProject:
    return ExternalProject.objects.create(
        name=name, client_name=client_name, deleted=deleted
    )


def internal_project_task_factory(
    *,
    name: str,
    completed: bool = False,
    project: InternalProject,
) -> InternalProjectTask:
    return InternalProjectTask.objects.create(
        name=name, completed=completed, project=project
    )
