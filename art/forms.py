from django.contrib.auth.models import User
from django import forms
from .models import *from .models import *

class Dmform(forms.ModelForm):
	class Meta:
		model = Messages
		exclude = ['sender', 'reciever', 'time_sent', 'read']