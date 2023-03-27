from django.contrib import admin


from django.contrib.auth.models import Group, User
from .models import Profile,Dweet,Like

class ProfileInLine(admin.StackedInline):
	model = Profile 
	extra=0

class UserAdmin(admin.ModelAdmin):
	model = User
	fields = ["username"]
	inlines = [ProfileInLine]
	
	
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.unregister(Group)
#admin.site.register(Profile);
admin.site.register(Dweet)
admin.site.register(Like)