from django.conf.urls import url
from .  import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
url(r'^$',views.home,name="home"),
url(r'^new_profile/$',views.new_profile,name='new_profile'),
url(r'^categories/$',views.categories,name='categories'),
url(r'^categories/(?P<cat_id>\d+)',views.categories_id,name='categories_id'),
url(r'^companyadd/(?P<comp_id>\d+)',views.company_add,name='company_add'),
url(r'^company/(?P<company_id>\d+)',views.company_id,name='company_id'),
url(r'^companyfeed/(?P<compani_id>\d+)',views.company_feed,name='company_feed'),
url(r'^new_post/$',views.new_post,name='new_post'),
url(r'^companydel/(?P<compdel_id>\d+)',views.company_delete,name='company_delete'),

]
if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
