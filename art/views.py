from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.
@login_required(login_url='accounts/login')
def home(request):
	companies=Company.objects.all()
	return render(request,'home.html',locals())

@login_required(login_url='accounts/login')
def categories(request):
	categories=Categories.objects.all()
	print(categories)
	return render(request,'categories.html',locals())
@login_required(login_url='accounts/login')
def categories_id(request,cat_id):
	category=Categories.objects.filter(id=cat_id)
	print(category)
	return render(request,'categories_id.html',locals())

@login_required(login_url='accounts/login')
def send_message(request):
	return render(request,'messages.html')

@login_required(login_url='/accounts/login')
def new_profile(request):
	current_user = request.user
	if request.method == 'POST':
		form = NewProfileForm(request.POST,request.FILES, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return redirect('home')

	else:
			form = NewProfileForm()
	return render(request, 'new_profile.html',{"form":form })

@login_required(login_url='/accounts/login')
def new_company(request):
	current_user = request.user
	if request.method == 'POST':
		form =NewNeigbor_hood_Form(request.POST,request.FILES)
		if form.is_valid():
			location = form.save(commit=False)
			location.user = current_user
			location.save()
			request.user.profile.neighbor_hood=location
			request.user.profile.save()
			return redirect('home')
	else:
			form = NewNeigbor_hood_Form()
	return render(request, 'new_location.html',{"form":form })


@login_required(login_url='/accounts/login')
def company_add(request,comp_id):
	UserProfile.objects.update(company=comp_id)
	return redirect('home')

@login_required(login_url='/accounts/login')
def company_delete(request,compdel_id):
	request.user.profile.company=None#
	request.user.profile.save()
	return redirect('categories')


@login_required(login_url='accounts/login')
def company_id(request,company_id):
	companies=Company.objects.filter(id=company_id)
	print(categories)
	return render(request,'company.html',locals())	

@login_required(login_url='/accounts/login')
def new_post(request):
	current_user = request.user
	if request.method == 'POST':
		form = NewPostForm(request.POST,request.FILES)
		if form.is_valid():
			article = form.save(commit=False)
			article.user = current_user
			article.save()
			request.user.profile.hoodpost=article
			request.user.profile.save()
			return redirect('home')
	else:
			form = NewPostForm()
	return render(request, 'new_post.html',{"form":form })	


@login_required(login_url='/accounts/login')
def company_feed(request,compani_id):
	compani=Company.objects.get(pk=compani_id)
	posts=compani.company_post.all()
	form = NewCommentForm()
	return render(request,'hood.html',locals())	