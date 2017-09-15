from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^register$', views.register, name ='reg_form'),
    url(r'^submit_registration$', views.submit_registration, name ='submit_reg'),
    url(r'^login_user$', views.login_user, name ='login_submit'),
    url(r'^logout$', views.logout, name ='logout'),
    url(r'^subscribe$', views.subscribe, name ='subscribe_submit'),
    url(r'^about$', views.about, name ='about'),
    url(r'^cart$', views.cart, name ='cart'),
    url(r'^contact$', views.contact, name ='contact'),
]