from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


def main(request):
    if request.method == 'POST':
        return redirect('login')
        #if:

       # elif:

      #  else:

    return render(request, 'temp/main.html', {})

def login(request): #login form
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid(): #check form for validation
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None: #check is there user with that nickname
                if user.is_active: #check user for activity
                    login(request, user)
                    return HttpResponse('Вы успешно авторизовались')
                else:
                    return HttpResponse('Аккаунт не существует')
            else:
                return HttpResponse('Логин не верный')
    else:
        form = LoginForm()
    return render(request, 'temp/acc/login.html', {'form':form})

def singup(request):#sing up form
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            profile = Profile.objects.create(user=new_user)
            return render(request, 'temp/acc/singup_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'temp/acc/singup.html', {'user_form': user_form})

def edit(request): #edit form
    if request.method == 'POST': #edit user info
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    #elif request.method == 'DELETE':

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'acс/edit.html', {'user_form': user_form,'profile_form': profile_form})

#def staticssocical(request):
   # return render(request, 'temp/staticssocical.html', {})
def registration(request):
    return None