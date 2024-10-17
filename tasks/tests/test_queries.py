from django.db.utils import IntegrityError
from django.test import TestCase

from tasks.queries import (
    ProjectType,
    get_all_projects,
    get_internal_projects_total_cost,
)
from tasks.tests.factories import external_project_factory, internal_project_factory


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


class TestExternalProjectModel(TestCase):
    def test_should_be_unique(self):
        external_project_factory(name="Project A", client_name="Client A")
        external_project_factory(name="Project A", client_name="Client A", deleted=True)
        external_project_factory(name="Project A", client_name="Client B")

        with self.assertRaises(IntegrityError):
            external_project_factory(name="Project A", client_name="Client A")
