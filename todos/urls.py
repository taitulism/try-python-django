from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_create_todo),
    path('<id>', views.edit_delete_todo)
]