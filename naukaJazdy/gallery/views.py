from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render

def gallery(request):
	return render(request, 'gallery.html')