from django import forms
from .models import Reservation
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'
	
class ReservationForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = ('information', 'date', 'time', 'category')
		widgets = {
            'date': DateInput(attrs={'class': 'form-control form-control-sm text-center rounded-0'}),
			'information': forms.Textarea(attrs={'class': 'form-control form-control-sm text-center rounded-0', 'placeholder': 'Wiadomość Dodatkowa'}),
			'time': forms.Select(attrs={'class':'form-control form-control-sm text-center rounded-0'}),
			'category': forms.Select(attrs={'class':'form-control form-control-sm text-center rounded-0'}),
        }
