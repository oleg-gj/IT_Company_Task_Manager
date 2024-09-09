from django.contrib.auth.models import AbstractUser
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tasks = models.ManyToManyField("Task", related_name="projects")

class Position(models.Model):
    name = models.CharField(max_length=100)


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    team = models.ForeignKey("Team", on_delete=models.CASCADE)

class Team(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class TaskType(models.Model):
    name = models.CharField(max_length=100)


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_complete = models.BooleanField(default=False)
    priority = models.TextChoices("Urgent", "Low", "Medium", "High")
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(Worker, related_name="workers")
