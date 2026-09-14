from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    # path('/detail/<int:question_id>', views.detail, name='detail'),
    path('write', views.write, name='write'),
    path('create', views.create, name='create'),
]
