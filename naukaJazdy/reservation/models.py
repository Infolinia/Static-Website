#-*- coding utf-8 -*-
from django.db import models
from django.conf import settings


TIME_CHOICES = (
	('08:00:00','08:00'),
	('10:00:00','10:00'),
	('12:00:00','12:00'),
	('14:00:00','14:00'),
	('16:00:00','16:00'),
)

CATEGORY_CHOICES = (
	('A','A'),
	('B','B'),
	('D','D'),
	('T','T'),
)

class Reservation(models.Model):
	information=models.TextField(max_length=50, verbose_name="Informacja do instruktora", null=True, blank=True)
	date=models.DateField(verbose_name="Data",null=True)
	time=models.CharField(verbose_name="Godzina",max_length=10,choices=TIME_CHOICES,default='08:00')
	category=models.CharField(verbose_name="Kategoria",max_length=10,choices=CATEGORY_CHOICES,default='A')
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
	def __unicode__(self):
		return self.information
	
	
