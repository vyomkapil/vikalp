from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Company, UserProfile, Branch


class RegistrationForm(UserCreationForm):
    contact_no = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

    def save(self, commit=True):
        data = self.cleaned_data

        user = super(RegistrationForm, self).save()
        user_profile = UserProfile(user=user, contact_no=data['contact_no'])
        user_profile.save()
        return user


class CompanyForm(forms.ModelForm):
    branch = forms.ModelChoiceField(
        queryset=Branch.objects.all().order_by('name'))

    class Meta:
        model = Company
        fields = ('name', 'title', 'about', 'proc', 'location', 'ctc', 'experience', 'branch')

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))