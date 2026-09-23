from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('write', views.write, name='write'),
    path('create', views.create, name='create'),
    path('question/detail/<int:q_id>', views.detail, name='detail'),
    path('delete/<int:q_id>', views.delete, name='delete'),
    path('edit/<int:q_id>', views.edit, name='edit'),
    path('update/<int:q_id>', views.update, name='update')
]