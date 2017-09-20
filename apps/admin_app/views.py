from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.core import serializers
from django.contrib import messages
from .models import Admins
import bcrypt, json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
  return render(request, 'admin_app/index.html')

@csrf_exempt
def login(request):
  print(request.body)
  data = json.loads(request.body)
  print(data['email'])
  email = data['email']
  password = data['password']
  print 'Email: ' + email + ', password: ' + password
  errors = Admins.objects.login_validator(data)
  print errors
  # if len(errors):
  #   for tag,error in errors.iteritems():
  #     messages.add_message(request, messages.ERROR, str(error))
  #   return redirect(reverse('admin_index'))
  # else:
  #   # request.session['id'] = Admins.objects.get(email = email).id
  #   #messages.add_message(request, messages.SUCCESS, "Successfully logged in!")
  #   return redirect(reverse('admin_mission_control'))
  return HttpResponse(errors, content_type='application/json')

def register_admin(request):
  first_name = request.POST['first_name']
  last_name = request.POST['last_name']
  email = request.POST['email']
  password = request.POST['password']
  confirm_pw = request.POST['confirm_pw']
  salt=bcrypt.gensalt()
  hashed_password = bcrypt.hashpw(request.POST['password'].encode(encoding='utf-8', errors='strict'), salt)
  errors = Admins.objects.register_validator(request.POST)
  print errors
  if len(errors):
    for tag,error in errors.iteritems():
      messages.add_message(request, messages.ERROR, str(error))
      return redirect(reverse('admin_index'))
  else: 
    admin = Admins.objects.create(first_name = first_name, last_name = last_name, email = email, password = hashed_password)
    # messages.add_message(request, messages.SUCCESS, "Successfully registered!")
    request.session['id'] = Admins.objects.get(email = email).id
    print ('*'*50)
    print Admins.objects.all()
    return redirect(reverse('admin_mission_control'))

def delete_admin(request):
  print 'LOOKAMEE'
  print request.POST['id']
  id = request.POST['id']
  Admins.objects.get(id = id).delete()
  return redirect(reverse('admin_mission_control'))

def edit_admin_page(request, id):
  print id
  print 'Where\'s the beef?'
  admins = Admins.objects.filter(id = id)
  print admins
  context = {
    'admins' : admins
  }
  data = serializers.serialize("json", admins)
  return HttpResponse(data, content_type='application/json')

def edit_admin(request):
  first_name = request.POST['first_name']
  last_name = request.POST['last_name']
  email = request.POST['email']
  password = request.POST['password']
  confirm_pw = request.POST['confirm_pw']
  salt=bcrypt.gensalt()
  hashed_password = bcrypt.hashpw(request.POST['password'].encode(encoding='utf-8', errors='strict'), salt)
  errors = Admins.objects.edit_admin_validator(request.POST)
  print errors
  if len(errors):
    for tag,error in errors.iteritems():
      messages.add_message(request, messages.ERROR, str(error))
      return redirect('/edit_admin_page/' + request.POST['id'])
  else:
    admin = Admins.objects.get(id = request.POST['id'])
    admin.first_name = first_name
    admin.last_name = last_name
    admin.email = email
    admin.password = hashed_password
    admin.save()
    return redirect(reverse('admin_mission_control'))

def mission_control(request):
  admins = Admins.objects.all()
  data = serializers.serialize("json", admins)
  context = {
    'admins' : admins
  }
  butter = {
    'butter' : 'butter'
  }
  return HttpResponse(data, content_type='application/json')

def logout(request):
  del request.session['id']
  return redirect(reverse('admin_index'))

def edit_users(request):
  return render(request, 'admin_app/edit_users.html')

def edit_products(request):
  return render(request, 'admin_app/edit_products.html')