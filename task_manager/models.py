from django.contrib.auth.models import AbstractUser
from django.db import models


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

    def __str__(self):
        return (
            f"User:{self.username}"
        )


class Team(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    workers = models.ManyToManyField(Worker)

    def __str__(self):
        return f"{self.name} ({self.project})"


class TaskType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_complete = models.BooleanField(default=False)
    priority = models.TextChoices("Urgent", "Low", "Medium", "High")
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(Worker, related_name="tasks")

    def __str__(self):
        return f"Task: {self.name} is complete {self.is_complete} "
