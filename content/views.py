from django.shortcuts import render
from .models import Project
from .forms import ProjectForm

def projects_list_view(request):
    projects = Project.objects.all()

    return render(request, "content/projects_list.html")

# Create your views here.

def project_new_view(request):

    if request.method == "POST":
        form = ProjectForm()
        if form.is_valid():
            project = form.save()
            return redirect("projects_list")
        else:
            form = ProjectForm()

    return render(request, "content/project_new.html", {"form":form})