from django.shortcuts import render
from django.views import generic

from task_manager.models import Team, Project, Worker, Task, TaskType, Position


def index(request):
    """View function for the home page of the site."""

    num_teams = Team.objects.count()
    num_projects = Project.objects.count()
    num_workers = Worker.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_teams": num_teams,
        "num_projects": num_projects,
        "num_workers": num_workers,
        "num_visits": num_visits + 1,
    }

    return render(
        request,
        "task_manager/index.html",
        context=context
    )


class TeamListView(generic.ListView):
    model = Team
    paginate_by = 5


class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 5


class WorkerListView(generic.ListView):
    model = Worker
    paginate_by = 5


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5

class TaskTypeListView(generic.ListView):
    model = TaskType
    paginate_by = 5

class PositionListView(generic.ListView):
    model = Position
    paginate_by = 5
