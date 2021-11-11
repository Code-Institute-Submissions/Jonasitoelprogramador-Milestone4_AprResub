from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Host
from hostofferings.models import offering
from django.contrib.auth.models import User
from .forms import HostCreationForm
from hostofferings.forms import OfferingForm, ImageForm
from accounts.forms import UserEmailForm
from django.forms.models import model_to_dict



@login_required()
def hostProfile(request):  
    hosts = Host.objects.all() 
    result_list = []
    for host in hosts:
        offerings = offering.objects.filter(host=host)
        offerings_list = list(offerings)
        for o in offerings_list:
            host_and_offering = [host] + [o]
            result_list += host_and_offering
    it = iter(result_list)
    zipped_tuples = zip(it, it)
    tuples = list(zipped_tuples)
    for x in tuples:
        if x[0] == request.user: 
            return x
    hoster = x[0]
    offer = x[1]
    return render(request, 'users/host_profile.html', {'host': hoster, 'offer': offer})


@login_required()
def hostProfileEdit(request):
    offeringz = offering.objects.all()
    userz = User.objects.all()
    result_list = []
    hosts = Host.objects.all()
    for h in hosts:
        if request.user == h.user:
            if request.method == 'POST':
                hostyForm = HostCreationForm(request.POST, instance = h)
                saveForm(hostyForm)
            else:    
                hostDict = {'nationality': h.nationality, 'first_language': h.first_language, 'location': h.location}
                host_filled_form = HostCreationForm(initial=hostDict)
    for o in offeringz:
        if request.user == o.host.user:
            off_obj = o
            if request.method == 'POST':
                offeryForm = OfferingForm(request.POST, instance = o)
                saveForm(offeryForm)
            else:
                offDict = {'work_category': o.work_category, 'work_details': o.work_details}
                offering_filled_form = OfferingForm(initial=offDict)
    for u in userz:
        if request.user == u:
            user_obj = u 
            if request.method == 'POST':
                print(request.POST)
                useryForm = UserEmailForm(request.POST, instance = u)
                saveForm(useryForm)
                return render(request, 'users/host_profile_edit.html')
            else:
                userDict = {'email': u.email}
                user_email_filled_form = UserEmailForm(initial=userDict) 
    return render(request, 'users/host_profile_edit.html', {"host_filled_form": host_filled_form, 
            'offering_filled_form': offering_filled_form, 'user_email_filled_form': user_email_filled_form, 'user_obj': user_obj,
            'off_obj': off_obj, 'ImageForm': ImageForm})


def saveForm(formToSave):
    counter = 0
    if formToSave.is_valid():
        formToSave.save()
        counter += 1
    else:
        print("not valid")


