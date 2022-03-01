"""define padrões de URL para learning_logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [

    path('', views.index, name='index'),  # página inicial
    path('topics/', views.topics, name='topics'),
    path('<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]
