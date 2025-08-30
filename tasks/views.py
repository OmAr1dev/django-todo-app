from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task


def task_list(request):
    """
    Display all tasks in descending order of creation.
    """
    tasks = Task.objects.all().order_by("-created_at")
    return render(request, "tasks/task_list.html", {"tasks": tasks})


def task_create(request):
    """
    Create a new task.
    """
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form})


def task_update(request, pk):
    """
    Update an existing task identified by primary key (pk).
    """
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/task_form.html", {"form": form})


def task_delete(request, pk):
    """
    Delete an existing task identified by primary key (pk).
    """
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(request, "tasks/task_confirm_delete.html", {"task": task})


def task_detail(request, pk):
    """Show full details for a single task."""
    task = get_object_or_404(Task, pk=pk)
    return render(request, "tasks/task_detail.html", {"task": task})
