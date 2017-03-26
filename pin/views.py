from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from board.models import UserReg

def login(request):
	c={}
	c.update(csrf(request))
	return render_to_response('Signin.html',c)
def auth_view(request):
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	try:
		entry=UserReg.objects.get(username=username,password=password)
	#if entry is not None:
		#auth.login(request,user)
		#return render(request,'pin.html',{'full_name':username})
		request.session['uso']=entry.username;
		return HttpResponseRedirect('/profile/')
	except:
		return HttpResponseRedirect('/invalid_login/')
def loggedin(request):
	return render_to_response('loggedin.html')
def invalid_login(request):
	return render_to_response('invalid_login.html')

