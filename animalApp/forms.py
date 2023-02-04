from dataclasses import fields
from django import forms
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import user, vet_visists, farm_owner, manager, farm_vertinary_officer, milk_production, animal_types, suppliment, vet_visist_prescription, AI_services
import datetime


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class AddVetForm(forms.Form):

    Manager_Name = forms.CharField(required=True, max_length=200)
    Owner_name = forms.CharField(required=True, max_length=200)
    Vet_Name = forms.CharField(required=True, max_length=200)
    joining_date = forms.DateField(initial=datetime.date.today)
    Address = forms.CharField(required=True)
    Vet_phone_number = forms.CharField(required=True)
    Status = forms.BooleanField(required=False, initial=True)


class AddManagerForm(forms.ModelForm):
    class Meta:
        model = manager
        fields = '__all__'


class contactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    subject = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'cols': 20, 'rows': 3}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ('user', 'rank', 'username')


class farm_owner_form(forms.ModelForm):
    class Meta:
        model = farm_owner
        fields = ('owner_name', 'owner_phone_number', 'owner_email')


class managerForm(forms.ModelForm):
    class Meta:
        model = manager
        fields = ('manager_name', 'manager_phone_number')


class farm_vertinary_officer_Form(forms.ModelForm):
    class Meta:
        model = farm_vertinary_officer
        fields = ('vet_name', 'vet_user_id', 'vet_phone_number', 'vet_email')


class animal_types_Form(forms.ModelForm):
    class Meta:
        model = animal_types
        fields = ('animal_ref', 'animal_name',
                  'animal_type_id', 'animal_status')


class milk_production_Form(forms.ModelForm):
    class Meta:
        model = milk_production
        exclude = ('production_total_quantity',)


class suppliment_Form(forms.ModelForm):
    class Meta:
        model = suppliment
        exclude = ('suppliment_production_added',)


class vet_visists_form(forms.ModelForm):
    class Meta:
        model = vet_visists
        fields = '__all__'


class vet_visist_prescription_Form(forms.ModelForm):
    class Meta:
        model = vet_visist_prescription
        fields = ('prescription_id', 'prescription_disease_name',
                  'prescription_vet_visist_id', 'prescription_description')


class AI_services_Form(forms.ModelForm):
    class Meta:
        model = AI_services
        fields = ('AI_animal_id', 'AI_vet_id', 'AI_comments')


class PerformanceSearchForm(forms.ModelForm):
    CHART_CHOICES = (
        ('bar graph', 'bar graph'),
        ('line Graph', 'line Graph')
    )
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)

    class Meta:
        model = milk_production
        fields = ('production_animal_id',)
