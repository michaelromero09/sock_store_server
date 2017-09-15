from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from ..manage_products.models import Products
import bcrypt
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'products_app/index.html')

def sale(request):
    return render(request, 'store_app/sale.html')