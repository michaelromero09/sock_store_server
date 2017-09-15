from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name ='products_main'),
    url(r'^products/sale$', views.sale, name ='products_sale'),
]
    