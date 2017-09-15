from __future__ import unicode_literals
from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class AdminManager(models.Manager):
    def register_validator(self, postData):
      errors = {}
      success = {}
      email_exists = Admins.objects.filter(email = postData['email'])
      if not postData["first_name"].isalpha():
          errors["first_name"] = "First name must contain only letters"
      if len(postData['first_name']) < 2:
          errors["first_name2"] = "First name should be longer than 2 characters"
      if not postData["last_name"].isalpha():
          errors["last_name"] = "Last name must contain only letters"
      if len(postData['last_name']) < 2:
          errors["last_name2"] = "Last name should be longer than 2 characters"
      if not EMAIL_REGEX.match(postData["email"]):
        errors["email"] = "Email is not valid"
      if email_exists:
        errors["email2"] = "Email already being used"
      if len(postData['password']) < 8:
        errors["password"] = "Password should be longer than 8 characters"
      if postData['password'] != postData["confirm_pw"]:
        errors["confirmation"] = "Password and password confirmation need to be matching"
      return errors

    def login_validator(self,postData):
      errors = {}
      db_password = Admins.objects.filter(email = postData['email']).values_list('password')
      email_exists = Admins.objects.filter(email = postData['email'])
      if not email_exists:
        errors["email"] = "Email address is not found in database"
      if len(postData['password']) == 0:
        errors['password'] = 'Please enter password'
        return errors
      hashed_password = bcrypt.hashpw(postData['password'].encode(encoding='utf-8', errors='strict'), str(db_password[0][0]))
      if db_password[0][0] != hashed_password:
        errors["password2"] = "Invalid password"
      print db_password,"*********", hashed_password
      print 'LOOKAMEE'
      print str(db_password[0][0])
      return errors

    def edit_admin_validator(self, postData):
      errors = {}
      success = {}
      email_exists = Admins.objects.filter(email = postData['email']).exclude(id = postData['id'])
      if not postData["first_name"].isalpha():
          errors["first_name"] = "First name must contain only letters"
      if len(postData['first_name']) < 2:
          errors["first_name2"] = "First name should be longer than 2 characters"
      if not postData["last_name"].isalpha():
          errors["last_name"] = "Last name must contain only letters"
      if len(postData['last_name']) < 2:
          errors["last_name2"] = "Last name should be longer than 2 characters"
      if not EMAIL_REGEX.match(postData["email"]):
        errors["email"] = "Email is not valid"
      if email_exists:
        errors["email2"] = "Email already being used"
      if len(postData['password']) < 8:
        errors["password"] = "Password should be longer than 8 characters"
      if postData['password'] != postData["confirm_pw"]:
        errors["confirmation"] = "Password and password confirmation need to be matching"
      return errors

class Admins(models.Model):
  first_name = models.TextField(max_length=255)
  last_name = models.TextField(max_length=255)
  email = models.TextField(max_length=255)
  password = models.TextField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = AdminManager()