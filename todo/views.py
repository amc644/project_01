from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo
from .forms import TodoForm

def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        