from django.contrib.auth.models import User
from django import forms
from .models import *from .models import *
from .models import *

class Dmform(forms.ModelForm):
	class Meta:
		model = Messages
		exclude = ['sender', 'reciever', 'time_sent', 'read']

class NewProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ['user'] 	
		
class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ['user']
