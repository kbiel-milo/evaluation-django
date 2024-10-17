from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.models import InternalProject, InternalProjectTask


class InternalProjectTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalProjectTask
        fields = (
            "id",
            "name",
            "completed",
        )


class InternalProjectDetailsSerializer(serializers.ModelSerializer):
    tasks = InternalProjectTaskSerializer(many=True, source="internalprojecttask_set")

    class Meta:
        model = InternalProject
        fields = (
            "id",
            "name",
            "tasks",
        )


class InternalProjectDetailsApi(APIView):
    @extend_schema(
        summary="Internal project details",
        description="Get details of an internal project with tasks sorted by completed status.",
        responses={
            200: InternalProjectDetailsSerializer,
        },
    )
    def get(self, request: Request, *args: str, **kwargs: str) -> Response:
        internal_project = InternalProject.objects.get(id=self.kwargs["project_id"])

        return Response(InternalProjectDetailsSerializer(internal_project).data)
