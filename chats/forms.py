from django import forms
from .models import MessageModel, CustomUser
    
class UserForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

    def clean_email(self):
        data = self.cleaned_data['email']
        if CustomUser.objects.filter(email=data).exists():
            raise forms.ValidationError("This email already exists!")
        
        return data
    
    def save(self, commit=True):
        user = super().save(commit=False)  # Bazaga saqlash uchun commit=False qilindi
        user.set_password(self.cleaned_data['password'])
        if commit:  # Agar commit=True bo'lsa, bazaga saqlanadi
            user.save()
        return user


class MessageForm(forms.ModelForm):

    class Meta:
        model = MessageModel
        fields = ("text", "to_user")