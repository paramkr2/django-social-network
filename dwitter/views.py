from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile,Dweet
from django.views import generic 
from .forms import DweetForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboard(request):
	form = DweetForm(request.POST or None );
	if request.method=='POST' and 'like' in request.POST :
		data = request.POST
		dweet = Dweet(id = data.get('pk')) 
		like = dweet.likes
		if data.get('like') == "like":
			
			like.userlist.add(request.user);
		elif data.get('like') == 'unlike':
			like.userlist.remove(request.user);
		like.save();
		
	elif request.method == 'POST':
		#form = DweetForm(request.POST)
		if form.is_valid():
			dweet = form.save(commit=False)
			dweet.user = request.user
			dweet.save()
			return redirect("dwitter:dashboard")
	#form = DweetForm()
	followed_dweets = Dweet.objects.filter(
		user__profile__in = request.user.profile.follows.all() 
		).order_by("-created_at")
	return render(request,"dwitter/dashboard.html", {"form":form} );
	
@login_required
def profile(request,pk):
	#django creates an anonymous user if not logged in
	# so for our testing we will make a user here
	if not hasattr( request.user, 'profile'):
		missing_profile = Profile(user=request.user);
		missing_profile.save();


	profile = Profile.objects.get( pk=pk )
	if request.method =="POST":
		current_user_profile = request.user.profile 
		data = request.POST 
		action = data.get('follow')
		if action == 'follow':
			current_user_profile.follows.add(profile)
		elif action == 'unfollow':
			current_user_profile.follows.remove(profile);
		current_user_profile.save()
	return render( request , "dwitter/profile.html",{"profile":profile} )
	
@login_required
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles": profiles})