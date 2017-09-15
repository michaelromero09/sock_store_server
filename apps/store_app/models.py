from __future__ import unicode_literals
from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, postData):
        user_errors = {}
        email_exists = Users.objects.filter(email = postData['email'])
        if not postData["first_name"].isalpha():
            user_errors["first_name"] = "First name must contain only letters"
        if len(postData['first_name']) < 2:
            user_errors["first_name2"] = "First name should be longer than 2 characters"
        if not postData["last_name"].isalpha():
            user_errors["last_name"] = "Last name must contain only letters"
        if len(postData['last_name']) < 2:
            user_errors["last_name2"] = "Last name should be longer than 2 characters"
        if not EMAIL_REGEX.match(postData["email"]):
            user_errors["email"] = "Email is not valid"
        if not postData["phone_num"].isnumeric():
            user_errors["phone_num"] = "Phone number must contain only numbers"
        if len(postData['phone_num']) < 10:
            user_errors["phone_num2"] = "Phone number is not valid"
        if len(postData['password']) < 8:
            user_errors["password"] = "Password should be longer than 8 characters"
        if postData['password'] != postData["confirm_pw"]:
            user_errors["confirmation"] = "Password and password confirmation need to be matching"
        return user_errors

    def login_validator(self,postData):
        errors = {}
        db_password = Users.objects.filter(email = postData['email']).values_list('password')
        email_exists = Users.objects.filter(email = postData['email'])
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

class AddressesManager(models.Manager):
  def address_validator(self, postData):
    address_errors = {}
    if len(postData["name"]) < 2:
      address_errors["name2"] = "Name should be longer than 2 characters"
    if len(postData['street']) < 3:
      address_errors["street"] = "You must enter a valid street address"
    if len(postData['city']) < 2:
      address_errors["city2"] = "City should be longer than 2 characters"
    if len(postData['zip_code']) < 5:
      address_errors["zip_code_length"] = "Zip code must contain 5 numbers"
    if not postData["zip_code"].isnumeric():
      address_errors["zip_code"] = "Please enter valid zip code"
    return address_errors

class Addresses(models.Model):
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    street2 = models.CharField(max_length=255)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AddressesManager()

class Subscribers(models.Model):
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    phone_num = models.IntegerField(default='')
    password = models.CharField(max_length=50)
    confirm_pw = models.CharField(max_length=50)
    address = models.OneToOneField(Addresses, on_delete =  models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    objects = UserManager()


    


