from django.urls import path
from .views import delete, home, detail, delete, create, update

app_name = 'todo'

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:todo_id>/', detail, name='detail'),
    path('delete/<int:todo_id>/', delete, name='delete'),
    path('create/', create, name='create'),
    path('update/<int:todo_id>/', update, name='update'),
]
