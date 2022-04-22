from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from register.models import RegisterForm
from django.contrib import messages
from django.shortcuts import render_to_response
from django.shortcuts import render

def login(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'login.html', c)

def view_auth(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request,user)
	else:
		messages.error(request, 'Błąd logowania, dane są nieprawidłowe.')
		c = {}
		c.update(csrf(request))
		return render(request, 'login.html', c)

	return render(request, 'home.html')


def logout(request):
	auth.logout(request)
	messages.success(request, 'Pomyslnie wylogowano z serwisu.')
	return render(request, 'login.html')

def create_user(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Konto zostało utworzone pomyślnie.')
	else: 
		form = RegisterForm();
		
	args = {}
	args.update(csrf(request))
	args['form'] = form

	return render(request, 'create_user.html', args)


