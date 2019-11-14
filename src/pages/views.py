from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	context = {"home_page": "active"}
	return render(request, 'pages/index.html', context)


def about(request):
	context = {"about_page": "active"}
	return render(request, 'pages/about.html', context)