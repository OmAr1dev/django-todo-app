from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    """
    Form for creating and updating Task instances.
    """

    class Meta:
        model = Task
        fields = ["title", "description", "completed"]
