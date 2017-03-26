from django import forms
from board.models import UserReg
from .models import UploadFile
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django.forms.utils import ErrorList
from django.utils.translation import ugettext_lazy as _
attrs_dict = {'class': 'required'}
# import re
# Create your models here.
# class UserRegForm(forms.Form):
# 	firstname=forms.CharField(max_length=200)
# 	username=forms.CharField(max_length=200)
# 	password=forms.CharField(max_length=200)
# 	email=forms.EmailField(max_length=70)
# 	description=forms.CharField(max_length=400)
# 	profilepic = forms.FileField(label='Select a file')

class UploadFileForm(forms.Form):
	
	description=forms.CharField(max_length=400)
	category=forms.CharField(max_length=200)
	docfile = forms.FileField(label='Select a file')
	link=forms.URLField()

class UserRegForm(forms.Form):
	firstname = forms.RegexField(regex=r'^[a-zA-Z]+$',max_length=30,widget=forms.TextInput(attrs=attrs_dict),label=_("Firstname"),error_messages={'invalid': _("The first name may contain only letters.")})
	username = forms.RegexField(regex=r'^[a-zA-Z][\w.@+-]+$',max_length=30,widget=forms.TextInput(attrs=attrs_dict),label=_("Username"),error_messages={'invalid': _("The username must begin with an alphabet and may contain only letters, numbers and @/./+/-/_ characters.")})
	email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,maxlength=75)),label=_("E-mail"))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),label=_("Password"))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),label=_("Password (again)"))
	location=forms.CharField(max_length=400)
	profilepic=forms.FileField(label='Select a profile picture')
	
	def clean_username(self):
		existing = UserReg.objects.filter(username__iexact=self.cleaned_data['username'])
		if existing.exists():
			raise forms.ValidationError(_("A user with that username already exists."))
		else:
			return self.cleaned_data['username']
	
	def clean(self):
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError(_("The two password fields did not match."))
		return self.cleaned_data
		
	def clean_email(self):
		if UserReg.objects.filter(email__iexact=self.cleaned_data['email']):
			raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
		return self.cleaned_data['email']
		


class ParagraphErrorList(ErrorList):
	def __unicode__(self):
		return self.as_paragraphs()

	def as_paragraphs(self):
		return "<p>%s</p>" % (",".join(e for e in self.errors))
	
class ForgotPassForm(forms.Form):
    username=forms.CharField(max_length=200)
    email = forms.EmailField()

class EditForm(forms.Form):
	firstname = forms.RegexField(regex=r'^[a-zA-Z]+$',max_length=30,widget=forms.TextInput(attrs=attrs_dict),label=_("Firstname"),error_messages={'invalid': _("The first name may contain only letters.")})
	email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,maxlength=75)),label=_("E-mail"))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),label=_("Password"))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),label=_("Password (again)"))
	location=forms.CharField(max_length=400)
	profilepic=forms.FileField(label='Select a profile picture')
	
	
	
	def clean(self):
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError(_("The two password fields did not match."))
		return self.cleaned_data

		


class ParagraphErrorList(ErrorList):
	def __unicode__(self):
		return self.as_paragraphs()

	def as_paragraphs(self):
		return "<p>%s</p>" % (",".join(e for e in self.errors))
	
