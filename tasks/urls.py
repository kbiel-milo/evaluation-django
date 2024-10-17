from django.urls import path

from tasks import apis

app_name = "tasks"

urlpatterns = [
    path(
        "internal-projects/<int:project_id>/",
        apis.InternalProjectDetailsApi.as_view(),
        name="internal-project-details",
    ),
]
