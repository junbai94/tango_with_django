# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import models
from .forms import CategoryForm

def index(request):
    category_list = models.Category.objects.order_by('-likes')[:5]
    context_dict = {'categories':category_list,}
    pages = models.Page.objects.order_by('-views')[:5]
    context_dict['pages'] = pages
    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_dict = {'num':5}
    return render(request, 'rango/about.html', context_dict)

def category(request, category_slug):
    
    context_dict = {}
    
    try:
        category = models.Category.objects.get(slug=category_slug)
        context_dict['category_name']=category.name
        
        pages = models.Page.objects.filter(category=category)
        
        context_dict['pages']=pages
        context_dict['category']=category
    except models.Category.DoesNotExist:
        pass
    
    return render(request, 'rango/category.html', context_dict)

def add_category(request):
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = CategoryForm()
    return render(request, 'rango/add_category.html', {'form':form})