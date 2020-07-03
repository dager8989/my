from django.shortcuts import render

def index(request):
	return  render(request, 'game/index.html')

def my(request):
	return  render(request, 'game/my.html')

