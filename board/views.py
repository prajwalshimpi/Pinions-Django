from django.shortcuts import render,HttpResponseRedirect,HttpResponse,render_to_response,RequestContext
from django.core.urlresolvers import reverse
from board.forms import UserRegForm,EditForm
from board.models import UserReg
from .forms import UploadFileForm
from .models import UploadFile
from django.forms.util import ErrorList
from .forms import ParagraphErrorList
from django.template.context_processors import csrf
from django.contrib import messages 
from django.core.mail import EmailMessage

# Create your views here.
def pinions(request):
	return render(request,'index.html')
	
def help_pin(request):
	if 'uso' in request.session:
		username=request.session['uso']
		user_obj=UserReg.objects.filter(username=username)
		log=1
		return render(request,'help.html',{'check':log,'user_objs':user_obj})
	else:
		log=0
		return render(request,'help.html',{'check':log})
def saveval(request):
	fields_dict={}
	if request.method == 'POST':
		form=UserRegForm(request.POST,request.FILES)
		if form.is_valid():
			firstname=request.POST.get('firstname','')
			username=request.POST.get('username','')
			email=request.POST.get('email','')
			password1=request.POST.get('password1','')
			password2=request.POST.get('password2','')
			description=request.POST.get('description','')
			profilepic=request.FILES['profilepic']
			location=request.POST.get('location','')
			user_obj=UserReg(firstname=firstname,username=username,email=email,password=password1,description=description,profilepic=profilepic,location=location)
			user_obj.save()
			return HttpResponseRedirect('/welcome/')
			#return render(request,'welcome.html')
		else:
			firstname=request.POST.get('firstname','')
			username=request.POST.get('username','')
			email=request.POST.get('email','')
			password1=request.POST.get('password1','')
			password2=request.POST.get('password2','')
			description=request.POST.get('description','')
			profilepic=request.FILES['profilepic']
			location=request.POST.get('location','')
			fields_dict={'firstname':firstname,'username':username,'email':email,'password1':password1,'password2':password2,'description':description,'profilepic':profilepic,'location':location}
			return render_to_response('Register.html',{'form':form,'fields_dict':fields_dict},context_instance=RequestContext(request))
	else:
		form=UserRegForm()
		messages.error(request, "Error")
		return render(request,'Register.html',{'form':form})

def welcome(request):
	
	return render(request,'welcome.html')
#def upload(request):
	#if request.method=='POST':
		#form=PictureForm(request.POST, request.FILES)
		#if form.is_valid():
			#username=request.username
			#return render_to_response('up.html')

def upload_file(request):
	if 'uso' in request.session:
		if request.method == 'POST':
			form = UploadFileForm(request.POST, request.FILES)
			if form.is_valid():
				usernames=request.session['uso']
				description=request.POST.get('description','')
				link=request.POST.get('link','')
				category=request.POST.get('category','')
				
				x=str(request.FILES['docfile'])
				doc=usernames +"&"+x
				newdoc = UploadFile(usernames=usernames,description=description,imglink=doc,category=category,docfile=request.FILES['docfile'],link=link)
				newdoc.save()
				return HttpResponseRedirect('/profile/')
			else:
				return HttpResponseRedirect('/upload_file/')
		else:
			#form = UploadFileForm()
			return HttpResponse("out of form")
		return render(request, 'upload.html', {'form': form})
	
	

def success_upload(request):
	return HttpResponseRedirect('/profile/')

def retrieve(request):
		if 'uso' not in request.session:
			log=0
			return HttpResponseRedirect('/pinions/')
			
		else:
			log=1
			objects=UploadFile.objects.filter(usernames=request.session['uso'])
			user_obj=UserReg.objects.filter(username=request.session['uso'])
			return render(request, 'pin.html', {'objects': objects,'user_obj':user_obj,'full_name' :request.session['uso'],'check':log})

def delete(request,del_link=""):
	del_object=UploadFile.objects.filter(imglink=del_link).delete()
	return HttpResponseRedirect('/profile/' )

def edit(request,edit_link=""):
	edit_obj=UploadFile.objects.filter(imglink=edit_link)
	return render(request, 'edit_upload.html',{'object': edit_obj,'usernames':request.session['uso']})
def upload(request):
	return render(request,'upload.html')
def update_file(request,edit_link=""):
	description=request.POST.get('description','')
	link=request.POST.get('link')

	x=str(request.FILES['docfile'])
	category=request.POST.get('category')
	doc=request.session['uso'] +"&"+x
	edit_obj=UploadFile.objects.filter(imglink=edit_link)
	edit_obj.delete()
	edit_obj=UploadFile(usernames=request.session['uso'],description=description,imglink=doc,category=category,docfile=request.FILES['docfile'],link=link)
	edit_obj.save()
	return HttpResponseRedirect('/profile/')
	
def retrieve_art(request):
	objs=UploadFile.objects.filter(category='Arts')
	
	if 'uso' in request.session:
		username=request.session['uso']
		user_obj=UserReg.objects.filter(username=username)
		
		log=1
		return render(request,'art.html',{'check':log,'user_objs':user_obj,'objs':objs})
	else:
		log=0
		return render(request,'art.html',{'check':log,'objs':objs})
	
def retrieve_food(request):
	objs=UploadFile.objects.filter(category='Food')
	if 'uso' in request.session:
		username=request.session['uso']
		user_obj=UserReg.objects.filter(username=username)
		log=1
		return render(request,'food.html',{'check':log,'user_objs':user_obj,'objs':objs})
	else:
		log=0
		return render(request,'food.html',{'check':log,'objs':objs})

def retrieve_other(request):
	objs=UploadFile.objects.filter(category='Other')
	if 'uso' in request.session:
		username=request.session['uso']
		user_obj=UserReg.objects.filter(username=username)
		log=1
		return render(request,'othercat.html',{'check':log,'user_objs':user_obj,'objs':objs})
	else:
		log=0
		return render(request,'othercat.html',{'check':log,'objs':objs})

def display_cat(request):
	if 'uso' in request.session:
		username=request.session['uso']
		user_obj=UserReg.objects.filter(username=username)
		log=1
		return render(request,'cat.html',{'check':log,'user_objs':user_obj})
	else:
		log=0
	return render(request,'cat.html',{'check':log})
	

	
def edit_profile(request):
	user_obj=UserReg.objects.filter(username=request.session['uso'])
	return render(request, 'edit_profile.html',{'user_obj':user_obj})
	
def update_profile(request):
	form=EditForm(request.POST,request.FILES)
	if form.is_valid():
		firstname=request.POST.get('firstname','')
		email=request.POST.get('email','')
		password1=request.POST.get('password1','')
		password2=request.POST.get('password2','')
		description=request.POST.get('description','')
		profilepic=request.FILES['profilepic']
		location=request.POST.get('location','')
		user_obj=UserReg.objects.filter(username=request.session['uso'])
		user_obj.delete()
		user_obj=UserReg(firstname=firstname,username=request.session['uso'],email=email,password=password1,description=description,profilepic=profilepic,location=location)
		user_obj.save()
		return HttpResponseRedirect('/profile/')
	else:
		firstname=request.POST.get('firstname','')
		email=request.POST.get('email','')
		password1=request.POST.get('password1','')
		password2=request.POST.get('password2','')
		description=request.POST.get('description','')
		profilepic=request.FILES['profilepic']
		location=request.POST.get('location','')
		user_obj=UserReg.objects.filter(username=request.session['uso'])
		
		return render_to_response('edit_profile.html',{'form':form,'user_obj':user_obj},context_instance=RequestContext(request))
		#form=EditForm()
		#messages.error(request, "Error")
		#return render(request,'edit_profile.html',{'form':form,},context_instance=RequestContext(request))
	
def pin_it(request,pin_link=""):
	if 'uso' in request.session:
		username=request.session['uso']
		pin_obj=UploadFile.objects.get(imglink=pin_link)
		x=str(pin_obj.docfile)
		doc=username+"&"+x
		new_obj=UploadFile(usernames=username,description=pin_obj.description,imglink=doc,category=pin_obj.category,docfile=pin_obj.docfile,link=pin_obj.link)
		new_obj.save()
		return HttpResponseRedirect('/profile/')
	else:
		return HttpResponseRedirect('/login/')
	
def logout(request):
	global log
	#auth.logout(request)
	if 'uso' in request.session:
		del request.session['uso']
		log=0;
	return render_to_response('logout.html')
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
		return HttpResponseRedirect('/login/')
def loggedin(request):
	return render_to_response('loggedin.html')
def invalid_login(request):
	return render_to_response('invalid_login.html')
def forgot_pass(request):
	if request.method == 'POST':
		username=request.POST.get('username','')
		email=request.POST.get('email','')
		user=UserReg.objects.get(username=username)
		subject="Password for Pinions"
		message="Hello "+user.username+",\nYour password for Pinions is '"+user.password+"'.\n\n-Regards:\n Pinions Team"
		email=EmailMessage(subject,message,to=[email])
		email.send()
		return render_to_response('mailsent.html')
	return render(request, 'forgot_pass.html', {'username': request.POST.get('username', ''),'email': request.POST.get('email', '')})
