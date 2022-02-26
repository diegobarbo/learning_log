"""define padrões de URL para learning_logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [

    path('', views.index, name='index'),  # página inicial
    path('topics/', views.topics, name='topics'),
    path('<int:topic_id>/', views.topic, name='topic'),
]
