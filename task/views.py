from django.shortcuts import render

def index(request, task_name="a"):
    return render(request, 'task/page.html', {'task_name': task_name})
