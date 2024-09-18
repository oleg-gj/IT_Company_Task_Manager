from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tasks = models.ManyToManyField("Task", related_name="projects")

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=100)
    workers = models.ManyToManyField("Worker", related_name="positions")

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    def get_absolute_url(self):
        return reverse("task_manager:worker-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"User:{self.username}"


class Team(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="teams")
    workers = models.ManyToManyField(Worker, related_name="teams")

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = (
        ("Urgent", "Urgent"),
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_complete = models.BooleanField(default=False)
    priority = models.CharField(
        choices=PRIORITY_CHOICES, default="Urgent", max_length=6
    )
    task_type = models.ForeignKey(
        TaskType, on_delete=models.CASCADE, related_name="tasks"
    )
    assigned_to = models.ManyToManyField(Worker, related_name="tasks")

    def __str__(self):
        return self.name
