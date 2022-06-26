from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from accounts.forms import AccountForm, ProfileForm, UserAdminCreationForm
from django.views.generic import View
from django.contrib import messages


def register(request):
    form_profile = ProfileForm(request.POST or None)
    form_user = UserAdminCreationForm(request.POST or None)
    form_account = AccountForm(request.POST or None)    

    if form_profile.is_valid() and form_user.is_valid() and form_account.is_valid():
        account = form_account.save(commit=False)
        account.status_account = True
        account.save()
        user = form_user.save(commit=False)
        user.is_active = True
        user.save()
        user.account.set([account])
        profile = form_profile.save(commit=False)
        profile.user = user
        profile.save()
        messages.success(request, 'create account success')
        return HttpResponseRedirect(reverse_lazy('accounts:login'))    
    
    context = {'form_profile': form_profile, 
                'form_user': form_user,
                'form_account': form_account,}        

    return render(request, 'accounts/register.html', context)
                