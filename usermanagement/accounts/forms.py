from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm

User = get_user_model()

class SignupForm(UserCreationForm):
    
    #password = forms.CharField(widget=forms.PasswordInput)
    #password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    email=forms.EmailField(max_length=255)
    name=forms.CharField(label='Name')
    address=forms.CharField()
    class Meta:
        model = User
        fields = ['email','name','address','password1','password2']

    def clean_email(self):
        '''
        Verify email is available.
        '''
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("This email is taken")
        return email


    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 is not None and password1 != password2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data