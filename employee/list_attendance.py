from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect

@login_required
def list_attendance(request):
    return render(request , 'list/list_attedance.html') 