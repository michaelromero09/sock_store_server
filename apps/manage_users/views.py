from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core import serializers
from ..store_app.models import Users, Addresses
import bcrypt

def get_all_users(request):
  print 'THIS thing'
  users = Users.objects.all()
  for user in users:
    print user.address.city
  data = serializers.serialize("json", users)
  return HttpResponse(data, content_type="application/json")

def get_user_by_id(request, id):
  print "I'm walkin' here"
  user = Users.objects.get(id = id)
  print user
  return 'Yeh'

def filter_user_by_id(id):
  return Users.objects.filter(id = id)

# def add_user(name, dept, style, design, material, price, cost):
#   Users.objects.create(name = name, dept = dept, style = style, design = design, material = material, price = price, cost = cost)
#   return 'Donesky'

def delete_user(id):
  print 'Deleting user with id: ' + str(id)
  Users.objects.get(id = id).delete()
  return 'Done-zo'

# Create your views here.
def index(request):
  print 'THAT thing'
  users = get_all_users()
  context = {
    'users' : users
  }
  return render(request, 'manage_users/index.html', context)

def edit_user_page(request, id):
  users = filter_user_by_id(id)
  print users[0].first_name
  context = {
    'users' : users
  }
  return render(request, 'manage_users/edit_user.html', context)

def edit_user(request):
  id = request.POST['id']
  first_name = request.POST['first_name']
  last_name = request.POST['last_name']
  email = request.POST['email']
  phone_num = request.POST['phone_num']
  password = request.POST['password']
  salt=bcrypt.gensalt()
  hashed_password = bcrypt.hashpw(request.POST['password'].encode(encoding='utf-8', errors='strict'), salt)
  confirm_pw = request.POST['confirm_pw']
  street = request.POST['street']
  city = request.POST['city']
  state = request.POST['state']
  zip_code = request.POST['zip_code']
  user = get_user_by_id(id)
  user.first_name = first_name
  user.last_name = last_name
  user.email = email
  user.phone_num = phone_num
  user.password = hashed_password
  user.save()
  address = user.address
  address.street = street
  address.city = city
  address.state = state
  address.zip_code = zip_code
  address.save()
  print 'Editing User'
  return redirect(reverse('manage_users_index'))

def delete_user_from_db(request):
  id = request.POST['id']
  print 'user id: ' + str(id)
  print delete_user(id)
  return redirect(reverse('manage_users_index'))