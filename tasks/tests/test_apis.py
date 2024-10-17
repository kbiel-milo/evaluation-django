from django.urls import reverse
from rest_framework.test import APITestCase

from tasks.tests.factories import (
    internal_project_factory,
    internal_project_task_factory,
)


class TestInternalProjectDetailsApi(APITestCase):
    def test_should_get_internal_project_details(self):
        internal_project = internal_project_factory(name="Project A")
        internal_project_task_a = internal_project_task_factory(
            name="Task A", project=internal_project, completed=False
        )
        internal_project_task_b = internal_project_task_factory(
            name="Task B", project=internal_project, completed=True
        )
        internal_project_task_c = internal_project_task_factory(
            name="Task C", project=internal_project, completed=False
        )

        response = self.client.get(
            reverse(
                "tasks:internal-project-details",
                kwargs={"project_id": internal_project.pk},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "id": internal_project.pk,
                "name": "Project A",
                "tasks": [
                    {
                        "id": internal_project_task_b.pk,
                        "name": "Task B",
                        "completed": True,
                    },
                    {
                        "id": internal_project_task_a.pk,
                        "name": "Task A",
                        "completed": False,
                    },
                    {
                        "id": internal_project_task_c.pk,
                        "name": "Task C",
                        "completed": False,
                    },
                ],
            },
        )
