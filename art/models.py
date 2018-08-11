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

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
	ID=models.CharField(max_length=100, null=True, blank=True)
	company=models.ForeignKey(Company, on_delete=models.CASCADE,related_name="company",null=True,blank=True)
	profilepicture = models.ImageField(upload_to='images/', blank=True,default="/black.png")
	secondary_email = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.user.username
	class Meta:
		ordering = ['user']
	def save_user(self):
		self.save()
	def delete_user(self):
		self.delete()		

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
				UserProfile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()

class Post(models.Model):
	post=models.CharField(max_length=100, null=True, blank=True)
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="adminpost",null=True,blank=True)
	company=models.ForeignKey(Company, on_delete=models.CASCADE,related_name="company_post",null=True,blank=True)

class Comments(models.Model):
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,related_name='user')
	comments = models.TextField()
	date_posted = models.DateTimeField(auto_now=True)
	post=models.ForeignKey(Post, on_delete=models.CASCADE,related_name="comments")

class Messages(models.Model):
	content = models.TextField()
	sender = models.ForeignKey(User, related_name='outbox')
	reciever = models.ForeignKey(User, related_name='inbox')
	read = models.BooleanField(default=False)
	time_sent = models.DateTimeField(auto_now_add=True)


	