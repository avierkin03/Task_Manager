from django.urls import path
from tasks import views

urlpatterns= [
    path('', views.TaskListView.as_view(), name="task-list"),
    path('task-create/', views.TaskCreateView.as_view(), name="task-create"),
    path('<int:pk>/', views.TaskDetailView.as_view(), name="task-detail"),
]

app_name = 'tasks'