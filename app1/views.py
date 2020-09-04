from django.shortcuts import render
from django.http import HttpResponse
from .models import DynamicMenu
# Create your views here.
def index(request):
	return HttpResponse('hello world')

def showMenu(request):
	menuList = DynamicMenu.objects.all()
	return render(request, 'app1/menuList.html', {'menuList': menuList})