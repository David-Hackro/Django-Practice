from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(requets):
    title = 'welcome to django curse!!'
    return render(requets, 'index.html', {
        'title': title
    })

def about(request):
    username = "David Hackro"
    return render(request, 'about.html', {
        'username': username
    })

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s </h2>" % username)

def projects(request):
    projects = list(Project.objects.values())
    #return JsonResponse(projects, safe = False)
    return render(request, 'projects.html', {
        'projects': projects
    })

def task(request):
    tasks = list(Task.objects.values())
    #task = Task.objects.get(id = id)
    #task = get_object_or_404(Task, id=id)
    #task = Task.objects.get(title = title)
    #return HttpResponse('Task: %s' % task.title)
    return render(request, 'tasks.html', {
        'tasks': tasks
    })
