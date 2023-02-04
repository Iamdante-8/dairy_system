from .forms import contactForm, PerformanceSearchForm, vet_visists_form, vet_visist_prescription_Form, AI_services_Form, SignUpForm, AddManagerForm, ProfileForm, farm_owner_form, farm_vertinary_officer_Form, managerForm, milk_production_Form, animal_types_Form, suppliment_Form
from .models import vet_visist_prescription, user, animal_types, AI_services, farm_vertinary_officer, milk_production, suppliment, manager, farm_owner, vet_visists
from .render import Render
from django.utils import timezone
from django.views.generic import View
from .utils import get_chart
from animalApp import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
import base64
from io import BytesIO
from turtle import color
from django import forms
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from matplotlib import colors
from animalApp.models import manager, farm_owner
from django.template.loader import get_template
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


def home(request):
    title = ''
    confirm_message = None
    form = contactForm(request.POST or None)
    if form.is_valid():
        receivers_list = ['duncanwachira53@gmail.com']
        subject = form.cleaned_data['subject']
        name = form.cleaned_data['name']
        comment = form.cleaned_data['message']
        emailFrom = form.cleaned_data['email']
        message = f'Name: {name}\nEmail Id: {emailFrom}\nMessage: {comment}'
        emailsender = settings.EMAIL_HOST_USER
        send_mail(subject, message, emailsender,
                  receivers_list, fail_silently=False)
        title = "Thanks!"+' '+name
        confirm_message = "Thanks for the message. We will get right back to you."
        form = None
    context = {'title': title, 'form': form,
               'confirm_message': confirm_message}
    temp = 'home.html'
    return render(request, temp, context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # If you want to login user after signup, than use this code
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def ai_list_owner(request):
    services = AI_services .objects.all()
    return render(request, 'owner/ailist.html', {'services': services})


@login_required
def prescription_list_owner(request):
    pres = vet_visist_prescription.objects.all()
    return render(request, 'owner/prescriptionlist.html', {'pres': pres})


@login_required
def addmanager(request):
    vl = manager.objects.only('manager_name')
    if request.method == 'POST':
        form = AddManagerForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('manager-list')
    else:
        form = AddManagerForm()
        return render(request, 'manager/addmanager.html', {'form': form, 'vl': vl})


@login_required
def managerlist(request):
    managers = manager.objects.all()
    return render(request, 'manager/managerlist.html', {'managers': managers})

# delete view for details


@login_required
def updatemanager(request, pk):
    managers = manager.objects.get(manager_id=pk)
    form = managerForm(instance=managers)

    if request.method == 'POST':
        form = managerForm(request.POST, instance=managers)
        if form.is_valid():
            form.save()
            return redirect("manager-list")
    return render(request, 'manager/updatemanager.html', {'form': form})


@login_required
def prescription_list(request):
    pres = vet_visist_prescription.objects.all()
    return render(request, 'manager/prescriptionlist.html', {'pres': pres})


@login_required
def ai_list(request):
    services = AI_services .objects.all()
    return render(request, 'manager/ailist.html', {'services': services})


@login_required
def deletemanager(request, pk):
    man = get_object_or_404(manager, pk=pk)
    if request.method == "POST":
        man.delete()
        return redirect('manager-list')
    return render(request, 'animals/animalslist.html', {'man': man})


@login_required
def addvetofficer(request):
    if request.method == 'POST':
        form = farm_vertinary_officer_Form(request.POST)
        # print("i am in addcustomer upper")
        if form.is_valid():
            # print("i am in addcustomer")
            form.save()
            return redirect('vet-list')
    else:
        form = farm_vertinary_officer_Form()
    return render(request, 'vetofficer/addvetofficer.html', {'form': form})


@login_required
def addai(request):
    if request.method == 'POST':
        form = AI_services_Form(request.POST)
        # print("i am in addcustomer upper")
        if form.is_valid():
            # print("i am in addcustomer")
            form.save()
            return redirect('ai-list')
    else:
        form = AI_services_Form()
    return render(request, 'vetofficer/addai.html', {'form': form})


@login_required
def ailist(request):
    services = AI_services .objects.all()
    return render(request, 'vetofficer/ailist.html', {'services': services})


@login_required
def deleteai(request, pk):
    ai = get_object_or_404(AI_services, pk=pk)
    if request.method == "POST":
        ai.delete()
        return redirect('ai-list')
    return render(request, 'vetofficer/ailist.html', {'ai': ai})


@login_required
def addvetvisists(request):
    if request.method == 'POST':
        form = vet_visists_form(request.POST)
        # print("i am in addcustomer upper")
        if form.is_valid():
            # print("i am in addcustomer")
            form.save()
            return redirect('visit-list')
    else:
        form = vet_visists_form()
    return render(request, 'vetofficer/addvisists.html', {'form': form})


@login_required
def addprescription(request):
    if request.method == 'POST':
        form = vet_visist_prescription_Form(request.POST)
        # print("i am in addcustomer upper")
        if form.is_valid():
            # print("i am in addcustomer")
            form.save()
            return redirect('prescription-list')
    else:
        form = vet_visist_prescription_Form()
    return render(request, 'vetofficer/addprescription.html', {'form': form})


@login_required
def prescriptionlist(request):
    pres = vet_visist_prescription.objects.all()
    return render(request, 'vetofficer/prescriptionlist.html', {'pres': pres})


def updateprescription(request, pk):
    preps = vet_visist_prescription.objects.get(prescription_id=pk)
    form = vet_visist_prescription_Form(instance=preps)

    if request.method == 'POST':
        form = vet_visist_prescription_Form(request.POST, instance=preps)
        if form.is_valid():
            form.save()
            return redirect("prescription-list")
    return render(request, 'vetofficer/updatprescription.html', {'form': form})


@login_required
def deleteprescription(request, pk):
    presc = get_object_or_404(vet_visist_prescription, pk=pk)
    if request.method == "POST":
        presc.delete()
        return redirect('prescription-list')
    return render(request, 'vetofficer/prescriptionlist.htm', {'presc': presc})


@login_required
def vetlist(request):
    vets = farm_vertinary_officer.objects.all()
    return render(request, 'vetofficer/vetlist.html', {'vets': vets})


@login_required
def updatevet(request, pk):
    vets = farm_vertinary_officer.objects.get(vet_id=pk)
    form = farm_vertinary_officer_Form(instance=vets)

    if request.method == 'POST':
        form = farm_vertinary_officer_Form(request.POST, instance=vets)
        if form.is_valid():
            form.save()
            return redirect("vet-list")
    return render(request, 'vetofficer/updatevet.html', {'form': form})


@login_required
def deletevet(request, pk):
    vet = get_object_or_404(farm_vertinary_officer, pk=pk)
    if request.method == "POST":
        vet.delete()
        return redirect('vet-list')
    return render(request, 'vetofficer/vetlist.html', {'vet': vet})


@login_required
def addanimal(request):
    cl = animal_types.objects.only('animal_ref')
    if request.method == "POST":
        form = animal_types_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animal-list')
    else:
        form = animal_types_Form()
    return render(request, 'animals/addanimal.html', {'form': form, 'cl': cl})


@login_required
def animalslist(request):
    animals = animal_types.objects.all()
    return render(request, 'animals/animalslist.html', {'animals': animals})


@login_required
def updateanimal(request, pk):
    animal = animal_types.objects.get(animal_id=pk)
    form = animal_types_Form(instance=animal)

    if request.method == 'POST':
        form = animal_types_Form(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect("animal-list")
    return render(request, 'animals/updateanimal.html', {'form': form})


@login_required
def deleteanimal(request, pk):
    animal = get_object_or_404(animal_types, pk=pk)
    if request.method == "POST":
        animal.delete()
        return redirect('animal-list')
    return render(request, 'animals/animalslist.html', {'animal': animal})


@login_required
def addsupplement(request):
    vl = suppliment.objects.only('suppliment_id')
    if request.method == 'POST':
        form = suppliment_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplement-list')
    else:
        form = suppliment_Form()
        return render(request, 'supplement/addsupplement.html', {'form': form, 'vl': vl})


@login_required
def supplimentlist(request):
    supps = suppliment.objects.all()
    return render(request, 'supplement/supplementlist.html', {'supps': supps})


@login_required
def updatesupplement(request, pk):
    sup = suppliment.objects.get(suppliment_id=pk)
    form = suppliment_Form(instance=sup)

    if request.method == 'POST':
        form = suppliment_Form(request.POST, instance=sup)
        if form.is_valid():
            form.save()
            return redirect("supplement-list")
    return render(request, 'supplement/updatesupplement.html', {'form': form})


@login_required
def deletesuppliment(request, pk):
    supp = get_object_or_404(suppliment, pk=pk)
    if request.method == "POST":
        supp.delete()
        return redirect('supplement-list')
    return render(request, 'supplement/supplementlist.html', {'supp': supp})


@login_required
def addmilkproduction(request):
    cl = milk_production.objects.only('production_total_quantity')
    if request.method == 'POST':
        form = milk_production_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('production-list')
    else:
        form = milk_production_Form()
    return render(request, 'production/addproduction.html', {'form': form, 'cl': cl})


@login_required
def productionlist(request):
    prods = milk_production.objects.all()
    return render(request, 'production/productionlist.html', {'prods': prods})


@login_required
def updateproduction(request, pk):
    prod = milk_production.objects.get(production_id=pk)
    form = milk_production_Form(instance=prod)

    if request.method == 'POST':
        form = milk_production_Form(request.POST, instance=prod)
        if form.is_valid():
            form.save()
            return redirect("production-list")
    return render(request, 'production/updateproduction.html', {'form': form})


@login_required
def updateai(request, pk):
    service = AI_services.objects.get(AI_service_id=pk)
    form = AI_services_Form(instance=service)

    if request.method == 'POST':
        form = AI_services_Form(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect("ai-list")
    return render(request, 'vetofficer/updateai.html', {'form': form})


@login_required
def deleteproduction(request, pk):
    prod = get_object_or_404(milk_production, pk=pk)
    if request.method == "POST":
        prod.delete()
        return redirect('production-list')
    return render(request, 'production/productionlist.html', {'prod': prod})


@login_required
def vet_visists_list(request):
    visists = vet_visists.objects.all()
    return render(request, 'vetofficer/visistlist.html', {'visists': visists})


@login_required
def update_vet_visit(request, pk):
    visit = vet_visists.objects.get(vet_visit_id=pk)
    form = vet_visists_form(instance=visit)

    if request.method == 'POST':
        form = vet_visists_form(request.POST, instance=visit)
        if form.is_valid():
            form.save()
            return redirect("visit-list")
    return render(request, 'vetofficer/updatevisit.html', {'form': form})


@login_required
def delete_visit(request, pk):
    visit = get_object_or_404(vet_visists, pk=pk)
    if request.method == "POST":
        visit.delete()
        return redirect('visit-list')
    return render(request, 'vetofficer/visistlist.html', {'visit': visit})

# reporting


class Pdf(View):

    def get(self, request):
        animals = animal_types.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'animals': animals,
            'request': request
        }
        return Render.render('animals/pdf.html', params)


class Pdf_visit(View):

    def get(self, request):
        visists = vet_visists.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'visists': visists,
            'request': request
        }
        return Render.render('vetofficer/pdf_vet.html', params)


class Pdf_manager(View):

    def get(self, request):
        mans = manager.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'mans': mans,
            'request': request
        }
        return Render.render('manager/pdf.html', params)


class Pdf_production(View):

    def get(self, request):
        prods = milk_production.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'prods': prods,
            'request': request
        }
        return Render.render('production/pdf.html', params)


class Pdf_vet(View):

    def get(self, request):
        vets = farm_vertinary_officer.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'vets': vets,
            'request': request
        }
        return Render.render('vetofficer/pdf.html', params)


class Pdf_supp(View):

    def get(self, request):
        supps = suppliment.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'supps': supps,
            'request': request
        }
        return Render.render('supplement/pdf.html', params)


class Pdf_ai(View):

    def get(self, request):
        services = AI_services.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'services': services,
            'request': request
        }
        return Render.render('vetofficer/ai_pdf.html', params)


class Pdf_prescription(View):

    def get(self, request):
        pres = vet_visist_prescription.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'pres': pres,
            'request': request
        }
        return Render.render('vetofficer/pre_pdf.html', params)
# ploting of graph using plotly package


@login_required
def production_graph(request):
    production_df = pd.DataFrame(milk_production.objects.all().values())

    production_df['production_date'] = production_df['production_date'].apply(
        lambda x: x.strftime('%Y-%m-%d'))
    x = production_df['production_id']
    y = production_df['production_total_quantity']
    plt.title("Animal Milk Production(per Production Id)", color='blue')
    plt.xlabel("Production Id", color='blue')
    plt.ylabel("Total milk production", color='blue')
    plt.xticks(np.arange(1, 100, step=1), rotation=45)
    plt.yticks(np.arange(0, max(y), step=5))
    sns.barplot(x, y, data=production_df)
    #axes = plt. gca()
    #axes. xaxis. label. set_size(15)
    #axes. yaxis. label. set_size(15)
    buf = BytesIO()
    plt.savefig(buf, format='png', dpi=300)
    plt.close()
    image_base64 = base64.b64encode(
        buf.getvalue()).decode('utf-8').replace('\n', '')
    buf.close()
    context = {
        'image_base64': image_base64
    }

    return render(request, 'production/production_graph.html', context)
# supplement production line graph


@login_required
def supplement_graph(request):
    supplement_df = pd.DataFrame(suppliment.objects.all().values())
    #x = supplement_df['suppliment_id']
    #y = supplement_df['']
    #plt.title("Milk Production after Supplement (by supplement_name)",color='blue')
    #plt.xlabel("Supplement Name",color='blue')
    #plt.ylabel("Milk production added after supplement",color='blue')
    #plt.xticks(rotation=15, color='blue')
    # plt.yticks(color='blue')
    sns.set_theme(style="whitegrid")
    g = sns.catplot(
        data=supplement_df, kind="bar",
        y='suppliment_production_added', x='suppliment_id',  hue="suppliment_name",
        ci="sd", palette="dark", alpha=.6, height=6)

    g.despine(left=True)
    plt.yticks(np.arange(0, 12, 2))
    plt.title('Supplement performance by Name')

    g.set_axis_labels("Production_id", "suppliment_production_added (litres)")
    g.legend.set_title("supplement_name")
    buf = BytesIO()
    plt.savefig(buf, format='png', dpi=300)
    plt.close()
    image_base64 = base64.b64encode(
        buf.getvalue()).decode('utf-8').replace('\n', '')
    buf.close()
    context = {
        'image_base64': image_base64
    }
    return render(request, 'supplement/supplement_graph.html', context)
    #axes = plt. gca()
    # axes.xaxis.label.set_size(10)
    # axes.yaxis.label.set_size(10)


# Search functionality


def animal_view(request):
    latest_animal = animal_types.objects.all()
    query = request.GET.get('q')
    if query:
        latest_animal = animal_types.objects.filter(
            query(animal_ref__icontains=query) |
            query(animal_status=query) |
            query(animal_name__icontains=query)
        )
    context = {
        'latest_animal ': latest_animal,
    }

    return render(request, 'animals/animalslist.html', context)
