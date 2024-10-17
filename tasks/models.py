from django.db import models


class InternalProject(models.Model):
    name = models.CharField(max_length=100)
    production_cost = models.FloatField()
    maintanance_cost = models.FloatField()

    def __str__(self):
        return f"Internal project: {self.name}"


class InternalProjectTask(models.Model):
    project = models.ForeignKey(InternalProject, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Internal project task: {self.name}"


class ExternalProject(models.Model):
    name = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)

    deleted = models.BooleanField(default=False)

    class Meta:
        # TODO: Name and client name should be unique together for non-deleted projects.
        pass

    def __str__(self):
        return f"External project: {self.name}"
