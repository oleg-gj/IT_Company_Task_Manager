from django.urls import path

from .views import (
    index,
    TeamListView,
    ProjectListView,
    WorkerListView,
    TaskListView,
    PositionListView,
    TaskTypeListView,
    TeamCreateView,
    ProjectCreateView,
    WorkerCreateView,
    TaskCreateView,
    PositionCreateView,
    TaskTypeCreateView,
    TeamDetailView,
    ProjectDetailView,
    WorkerDetailView,
    TaskDetailView,
    PositionDetailView,
    TaskTypeDetailView,
    TeamDeleteView,
    TeamUpdateView,
    ProjectUpdateView,
    ProjectDeleteView,
    WorkerUpdateView,
    WorkerDeleteView,
    TaskUpdateView,
    TaskDeleteView,
    PositionUpdateView,
    PositionDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("team/", TeamListView.as_view(), name="team-list"),
    path("team/<int:pk>/", TeamDetailView.as_view(), name="team-detail"),
    path("team/create/", TeamCreateView.as_view(), name="team-create"),
    path("team/update/<int:pk>/", TeamUpdateView.as_view(), name="team-update"),
    path("team/delete/<int:pk>/", TeamDeleteView.as_view(), name="team-delete"),
    path("project/", ProjectListView.as_view(), name="project-list"),
    path(
        "project/<int:pk>/",
        ProjectDetailView.as_view(),
        name="project-detail"
    ),
    path("project/create/", ProjectCreateView.as_view(), name="project-create"),
    path(
        "project/update/<int:pk>/",
        ProjectUpdateView.as_view(),
        name="project-update"
    ),
    path(
        "project/delete/<int:pk>/",
        ProjectDeleteView.as_view(),
        name="project-delete"
    ),
    path("worker/", WorkerListView.as_view(), name="worker-list"),
    path("worker/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("worker/create/", WorkerCreateView.as_view(), name="worker-create"),
    path(
        "worker/update/<int:pk>/",
        WorkerUpdateView.as_view(),
        name="worker-update"
    ),
    path(
        "worker/delete/<int:pk>",
        WorkerDeleteView.as_view(),
        name="worker-delete"
    ),
    path("task/", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("position/",PositionListView.as_view(), name="position-list"),
    path(
        "position/<int:pk>/",
        PositionDetailView.as_view(),
        name="position-detail"
    ),
    path(
        "position/create/",
        PositionCreateView.as_view(),
        name="position-create"
    ),
    path(
        "position/update/<int:pk>/",
        PositionUpdateView.as_view(),
        name="position-update"
    ),
    path(
        "position/delete/<int:pk>/",
        PositionDeleteView.as_view(),
        name="position-delete"
    ),
    path(
        "tasktype/",
        TaskTypeListView.as_view(),
        name="tasktype-list"
    ),
    path(
        "tasktype/<int:pk>/",
        TaskTypeDetailView.as_view(),
        name="tasktype-detail"
    ),
    path(
        "tasktype/create/",
        TaskTypeCreateView.as_view(),
        name="tasktype-create"
    ),
    path(
        "tasktype/update/<int:pk>/",
        TaskUpdateView.as_view(),
        name="tasktype-update"
    ),
    path(
        "tasktype/delete/<int:pk>/",
        TaskDeleteView.as_view(),
        name="tasktype-delete"
    ),
]

app_name = "task_manager"
