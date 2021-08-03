from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register(request):
    form=UserCreationForm()
    form=UserCreationForm(request,'users/register.html', {'form':form})
