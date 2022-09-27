from dataclasses import field
from xml.parsers.expat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from skill_tracker import models
from api import models as apiModels



# Create your forms here.

# class NewUserForm(UserCreationForm):
# 	email = forms.EmailField(required=True)

# 	class Meta:
# 		model = User
# 		fields = ("username", "email", "password1", "password2")

# 	def save(self, commit=True):
# 		user = super(NewUserForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user

class EditUserForm(ModelForm):
	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "email")
		exclude = ("user_id", "archived")
		labels = {
			"username": '',
			"first_name": '',
			"last_name": '',
			"email": '',
		}
		widgets = {
			"username": forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
			"first_name": forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
			"last_name": forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
			"email": forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}),
		}
		help_texts = {
            "username":None,
        }

# class UserLoginForm(ModelForm):
# 	class Meta:
# 		model = User
# 		fields = ("username", "password")
# 		labels = {
# 			"username": '',
# 			"password": '',
# 		}
# 		widgets = {
# 			"username": forms.TextInput(attrs={'class':'form-control', 'placeholder':'Who ye be?'}),
# 			"password": forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Vats da passvord?'}),
# 		}
# 		help_texts = {
#             "username":None,
#         }

# class TeamManagementDashboard(ModelForm):
# 	class Meta:
# 		model = apiModels.Team
# 		fields = ("name",)

class AddTeamForm(ModelForm):
	class Meta:
		model = apiModels.Team
		fields = ('name','description')
		labels = {
			"name": '',
			"description": '',
		}
		
		widgets = {
			"name": forms.TextInput(attrs={'class':'form-control', 'placeholder':'Team Name'}),
			"description": forms.Textarea(attrs={'class':'form-control', 'rows':'5', 'placeholder':'Describe your team.'}),
		}
		help_texts = {
            "name":None,
        }