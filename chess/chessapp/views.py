from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.http import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Games
from .ai import *
import hashlib 





@login_required
def index(request):
    return HttpResponse("test page")

def signup(request):
	if request.method != "POST":
		return render(request, "registration/signup.html", {"error":"sign up here!"})


	user=request.POST.get("username")
	ans=User.objects.filter(username=user)
	error = ""
	if ans:
		error="This username is taken"
	email=request.POST.get("email")
	ans=User.objects.filter(email=email)
	if ans:
		error="Your email is already taken"
	pass1=request.POST.get("password")
	pass2=request.POST.get("repeatpassword")
	if pass1!=pass2:
		error="passwords do not match"
	if error :
		return render(request, "registration/signup.html", {"error":error})
	usr=User.objects.create_user(user,email,pass1)
	usr.save()
	game=Games(user=usr)
	game.save()
	link="http://"+request.META["HTTP_HOST"] + "/activate/" + user +"/"+hashlib.sha1((str(usr.id)+email+user).encode()).hexdigest()
	send_mail("activate","activate your account here."+link,"icp95.project@gmail.com",[email])
	return HttpResponse("user is created!")

@login_required
def game(request):
	imgs=[]
	user = request.user
	if user.first_name!="activated":
		return HttpResponse("user is not activated!")
	game = Games.objects.get(user = user)
	content = {}
	if(request.method == "POST"):
		mv=request.POST.get("move")
		test=AI(game.status)
		if not test.check_correct_move(mv):
			content['error']="Your move is not possible"
		else:
			ai_move=test.alphabeta(4,-100000000,+100000000,True)
			if ai_move[1]==None:
				if test.ai_king_in_danger() :
					content['error']="YOU WON THE GAME!"
				else:
					content['error']="The Game is tied!"
				return render(request,"registration/game.html",content)
			test.change_status(ai_move[1])
			game.status=test.convert_matrix()
			game.save()
			if len(test.final_user_moves())==0 :
				if test.user_king_in_danger():
					content['error']="you lost the game..."
				else:
					content['error']="The Game is tied!"
				return render(request,"registration/game.html",content)
	status=game.status
	for i in status.split("/")[:8]:
		tmp=[]
		for j in i :
			if(j == "."):
				tmp.append("e.png")
			elif(j.islower()):
				tmp.append(j+".png")
			else:
				tmp.append("w"+j+".png")

		imgs.append(tmp)

	content["dead"] = []
	for i in status.split("/")[8:]:
		for j in i:
			if(j.islower()):
				content["dead"].append(j+".png")
			else:
				content["dead"].append("w"+j+".png")
	content["state"] = imgs
	return render(request, "registration/game.html", content)
def activate(request):
	username=request.path.split("/")[-2]
	userhash=request.path.split("/")[-1]
	user=User.objects.get(username=username)
	if userhash==hashlib.sha1((str(user.id)+user.email+user.username).encode()).hexdigest() :
		user.first_name = "activated"
		user.save()
		return HttpResponse("user activated!")
	else:
		return HttpResponse("user not activated!")
def profile(request):
	return HttpResponseRedirect(reverse("game"))



# [ ['R.png', 'N.png', ... , 'R.png'] ]
#   ['P.png', 'P.png', ... , 'P.png']
# . 
# .
# .
# .
# .
# ]