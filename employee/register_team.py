from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect

@login_required
def register_new_team(request):
    return render(request , 'register/register_new_team.html') 