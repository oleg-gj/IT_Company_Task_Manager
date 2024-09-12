from django.urls import path

from .views import (
    index, TeamListView, ProjectListView, WorkerListView, TaskListView,
    PositionListView, TaskTypeListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("team", TeamListView.as_view(), name="team-list"),
    path("project", ProjectListView.as_view(), name="project-list"),
    path("worker", WorkerListView.as_view(), name="worker-list"),
    path("task", TaskListView.as_view(), name="task-list"),
    path("position",PositionListView.as_view(), name="position-list"),
    path("tasktype",TaskTypeListView.as_view(), name="tasktype-list"),
]

app_name = "task_manager"