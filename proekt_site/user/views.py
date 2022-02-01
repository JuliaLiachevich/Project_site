from django.shortcuts import  render, redirect
from django.contrib import  auth
from django.template.context_processors import csrf
from .forms import RegisterUserForm

def create(request):
    return render(request, 'user/create.html')

def login(request):
    args={}
    args.update(csrf(request))
    if request.POST:
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/../restoran')
        else:
            args ['login_error']='Пользователь не найден'
            return render(request,'user/login.html', args)
    else:
        return render(request,'user/login.html', args)

def logaut(reguest):
    auth.logout(reguest)
    return redirect('/')

def register (reguest):
    args={}
    args.update(csrf(reguest))
    args['form']=RegisterUserForm()
    if reguest.POST:
        newuser_form=RegisterUserForm(reguest.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser=auth.authenticate(username=newuser_form.cleaned_data['username'],
                                      password=newuser_form.cleaned_data['password2'])
            auth.login(reguest, newuser)
            return redirect('/../restoran')
        else:
            args['form']=newuser_form
    return render(reguest,'user/register_user.html', args)
