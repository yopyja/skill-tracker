from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from skill_tracker import models



# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class EditUserForm(ModelForm):
	
	class Meta:
		model = models.User
		fields = ("first_name", "last_name", "prefix", "position")
		exclude = ("user_id", "archived")
		labels = {
			"first_name": '',
			"last_name": '',
			"prefix": '',
			"position": '',
		}
		widgets = {
			"first_name": forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
			"last_name": forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
			"prefix": forms.TextInput(attrs={'class':'form-control', 'placeholder':'Prefix'}),
			"position": forms.TextInput(attrs={'class':'form-control', 'placeholder':'Duty Position'}),
		}