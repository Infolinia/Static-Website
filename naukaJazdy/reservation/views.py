from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from reservation.models import Reservation
from .forms import ReservationForm
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.shortcuts import render
from django.contrib import messages

def reserve(request):
	if request.method == "POST":
		rf = ReservationForm(request.POST)
		if rf.is_valid():
			rf.instance.user = request.user
			rf.save()
			args = {}
			args.update(csrf(request))
			args['form'] = rf
			messages.success(request, 'Rezerwacja przebiegła pomyślnie.')
			return render(request, 'reserve.html', args)
		
		return HttpResponseRedirect('/reserve/invalid/')
	else: 
		rf = ReservationForm()
		
	args = {}
	args.update(csrf(request))
	args['form'] = rf

	return render(request, 'reserve.html', args)


def my(request):
	return render(request, 'my.html',{'reservations' : Reservation.objects.filter(user_id=request.user.id)})



