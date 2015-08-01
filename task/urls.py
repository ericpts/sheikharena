from django.conf.urls import url
from task import views

urlpatterns = [
    url(r'^(?P<task_name>\w+)', views.index, name='task'),
]
