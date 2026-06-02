from django.shortcuts import render,redirect
from .models import Project
from .forms import ProjectForm

def projects_list(request):
    projects=Project.objects.all()
    context={'projects':projects}
    return render(request,'portfolio/index.html',context)

def create_project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list_projects')
    else:
        form = ProjectForm()

    return render(request, 'portfolio/create_project.html', {'form': form})