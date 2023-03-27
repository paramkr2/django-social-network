# users/forms.py

from django.contrib.auth.forms import UserCreationForm
from django import forms
class CustomUserCreationForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(CustomUserCreationForm, self).__init__(*args, **kwargs)
		for name, field in self.fields.items():
			#if field.widget.__class__ == forms.widgets.TextInput:
			if 'class' in field.widget.attrs:
				field.widget.attrs['class'] += 'input'
			else:
				field.widget.attrs.update({'class':'input'})
	class Meta(UserCreationForm.Meta):
		fields = UserCreationForm.Meta.fields + ("email",)