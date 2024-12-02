from django.shortcuts import render

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

def register(request):
    return render(request, 'accounts/register.html')

def profile(request):
    return render(request, 'accounts/profile.html')

def edit_profile(request):
    return render(request, 'accounts/edit_profile.html')

def change_password(request):
    return render(request, 'accounts/change_password.html')

def forgot_password(request):
    return render(request, 'accounts/forgot_password.html')

def reset_password(request):
    return render(request, 'accounts/reset_password.html')