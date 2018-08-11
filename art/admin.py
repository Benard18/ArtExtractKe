from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Company)
admin.site.register(Messages)
admin.site.register(Comments)
admin.site.register(Categories)
admin.site.register(Post)
