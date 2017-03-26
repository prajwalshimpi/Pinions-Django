from django.contrib import admin

# Register your models here.
from .models import UserReg
from .models import UploadFile


class UserRegAdmin(admin.ModelAdmin):
	list_display=('firstname','username','email','password','description','location','profilepic')

class UploadFileAdmin(admin.ModelAdmin):
	list_display=('usernames','description','docfile','category','link','imglink')

admin.site.register(UserReg,UserRegAdmin)
admin.site.register(UploadFile,UploadFileAdmin)