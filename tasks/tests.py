from django.test import TestCase
from tasks.models import InternalProject, ExternalProject
from tasks.queries import (
    get_all_projects,
    ProjectType,
    get_internal_projects_total_cost,
)
from django.db.models import QuerySet
import warnings

from django.db.utils import IntegrityError


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


class TestGetAllProjectsTotalCost(TestCase):
    def test_should_get_all_projects_total_cost(self):
        internal_project_factory(
            name="Project A", production_cost=100, maintanance_cost=200
        )
        internal_project_factory(
            name="Project C", production_cost=300, maintanance_cost=400
        )
        external_project_factory(name="Project B", client_name="Client name")

        total_cost = get_internal_projects_total_cost()

        self.assertEqual(total_cost, 1000.0)


class TestGetAllProjects(TestCase):
    def test_should_get_all_projects(self):
        internal_project_a = internal_project_factory(name="Project A")
        internal_project_c = internal_project_factory(name="Project C")
        external_project_b = external_project_factory(
            name="Project B", client_name="Client name"
        )

        projects = get_all_projects()

        self.assertEqual(
            list(projects),
            [
                {
                    "id": internal_project_a.pk,
                    "name": "Project A",
                    "type": ProjectType.INTERNAL.value,
                },
                {
                    "id": external_project_b.pk,
                    "name": "Project B",
                    "type": ProjectType.EXTERNAL.value,
                },
                {
                    "id": internal_project_c.pk,
                    "name": "Project C",
                    "type": ProjectType.INTERNAL.value,
                },
            ],
        )

    def test_could_return_a_queryset(self):
        projects = get_all_projects()

        if not isinstance(projects, QuerySet):
            warnings.warn("Bonus points await for returning a queryset :)")


class TestExternalProjectModel(TestCase):
    def test_should_be_unique(self):
        external_project_factory(name="Project A", client_name="Client A")
        external_project_factory(name="Project A", client_name="Client A", deleted=True)
        external_project_factory(name="Project A", client_name="Client B")

        with self.assertRaises(IntegrityError):
            external_project_factory(name="Project A", client_name="Client A")
