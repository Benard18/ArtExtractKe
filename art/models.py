from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Categories(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	profilepicture = models.ImageField(upload_to='png/', blank=True)
	def __str__(self):
		return self.name
class Company(models.Model):
	name=models.CharField(max_length=100, null=True, blank=True)
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="company_admin",null=True,blank=True)
	contacts=models.CharField(max_length=100, null=True, blank=True)
	location=models.CharField(max_length=100, null=True, blank=True)
	category=models.ForeignKey(Categories, on_delete=models.CASCADE,related_name="company_category",null=True,blank=True)
	profilepicture = models.ImageField(upload_to='company/', blank=True)


	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']	

	def save_company(self):
		self.save()	
