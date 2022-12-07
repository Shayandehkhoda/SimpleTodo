from django import forms


class UserRegistrationForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField(required=False)
	password = forms.CharField(widget=forms.PasswordInput())
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)


class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())