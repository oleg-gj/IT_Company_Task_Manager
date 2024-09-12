from django.contrib import admin

from task_manager.models import Task, Project, Position, Worker, Team, TaskType

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Position)
admin.site.register(Worker)
admin.site.register(Team)
admin.site.register(TaskType)
