from django.shortcuts import render

# Create your views here.

from .models import Customer

def show_projects(request):
	customers = Customer.objects.all()
	
	return render(request, 'timekeeper/show_project_list.html', {'customers':customers})
