from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from task_manager.forms import (
    TaskNameSearchForm,
    WorkerNameSearchForm,
    WorkerCreationForm,
    WorkerUpdateForm,
    TaskUpdateForm
)

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


class TeamDetailView(generic.DetailView):
    model = Team


class TeamCreateView(generic.CreateView):
    model = Team
    fields = "__all__"
    success_url = reverse_lazy("task_manager:team-list")


class TeamUpdateView(generic.UpdateView):
    model = Team
    fields = "__all__"
    success_url = reverse_lazy("task_manager:team-list")


class TeamDeleteView(generic.DeleteView):
    model = Team
    success_url = reverse_lazy("task_manager:team-list")


class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 5


class ProjectDetailView(generic.DetailView):
    model = Project


class ProjectCreateView(generic.CreateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("task_manager:project-list")


class ProjectUpdateView(generic.UpdateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("task_manager:project-list")


class ProjectDeleteView(generic.DeleteView):
    model = Project
    success_url = reverse_lazy("task_manager:project-list")


class WorkerListView(generic.ListView):
    model = Worker
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        first_name = self.request.GET.get("first_name", "")
        context["first_name"] = first_name
        context["search_form"] = WorkerNameSearchForm(
            initial={"first_name": first_name}
        )
        return context

    def get_queryset(self):
        queryset = Worker.objects.all()
        form = WorkerNameSearchForm(self.request.GET)

        if form.is_valid():
            queryset = queryset.filter(
                first_name__icontains=form.cleaned_data["first_name"]
            )
        return queryset


class WorkerDetailView(generic.DetailView):
    model = Worker


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("task_manager:worker-list")


class WorkerUpdateView(generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm

    def get_success_url(self, **kwargs):
        return reverse("task_manager:worker-detail",
                       kwargs={'pk': self.kwargs['pk']})


class WorkerDeleteView(generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("task_manager:worker-list")


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["name"] = name
        context["search_form"] = TaskNameSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Task.objects.all()
        form = TaskNameSearchForm(self.request.GET)

        if form.is_valid():
            queryset = queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task_manager:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy("task_manager:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_manager:task-list")


class TaskTypeListView(generic.ListView):
    model = TaskType
    paginate_by = 5


class TaskTypeDetailView(generic.DetailView):
    model = TaskType


class TaskTypeCreateView(generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("task_manager:tasktype-list")


class TaskTypeUpdateView(generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("task_manager:tasktype-list")


class TaskTypeDeleteView(generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("task_manager:tasktype-list")


class PositionListView(generic.ListView):
    model = Position
    paginate_by = 5


class PositionDetailView(generic.DetailView):
    model = Position


class PositionCreateView(generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task_manager:position-list")


class PositionUpdateView(generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task_manager:position-list")


class PositionDeleteView(generic.DeleteView):
    model = Position
    success_url = reverse_lazy("task_manager:position-list")
