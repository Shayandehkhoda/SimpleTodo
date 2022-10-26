from django import forms


class UserRegistrationForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField(required=False)
	password = forms.CharField()
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)


class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()