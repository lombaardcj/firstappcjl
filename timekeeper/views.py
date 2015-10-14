from django.shortcuts import render

# Create your views here.

def show_projects(request):
	return render(request, 'timekeeper/show_project_list.html', {})
