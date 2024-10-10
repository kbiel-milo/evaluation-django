from django.db import models


class InternalProject(models.Model):
    name = models.CharField(max_length=100)

    production_cost = models.FloatField()
    maintanance_cost = models.FloatField()

    def __str__(self):
        return f"Internal project: {self.name}"


class ExternalProject(models.Model):
    name = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)

    def __str__(self):
        return f"External project: {self.name}"
