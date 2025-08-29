from django.db import models

# Create your models here.


class Task(models.Model):
    """
    Represents a single task in the To-Do application.

    Attributes:
        title (str): The title or name of the task (max 200 characters).
        description (str): Optional detailed description of the task.
        completed (bool): Whether the task is completed or not. Defaults to False.
        created_at (datetime): Timestamp when the task was created. Set automatically.
        updated_at (datetime): Timestamp when the task was last updated. Set automatically.
    """

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the Task instance.
        """
        return self.title
