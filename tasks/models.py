from django.db import models
from django.contrib.auth.models import User

# Модель Завдання
class Task(models.Model):
    STATUS_CHOISES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    ]

    PRIORITY_CHOISES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("hight", "Hight"),
    ]

    title = models.CharField(max_length=256)
    description = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS_CHOISES, default="todo")
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOISES, default="low")
    due_date = models.DateField(null = True, blank = True)
    creator = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "tasks")

    def __str__(self):
        return self.title