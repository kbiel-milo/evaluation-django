# Generated by Django 4.2.2 on 2024-10-17 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0002_externalproject_deleted"),
    ]

    operations = [
        migrations.CreateModel(
            name="InternalProjectTask",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("completed", models.BooleanField(default=False)),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tasks.internalproject",
                    ),
                ),
            ],
        ),
    ]