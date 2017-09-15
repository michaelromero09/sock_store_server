from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.get_all_products, name = 'manage_products_index'),
    url(r'^add_product_page$', views.add_product_page, name = 'manage_products_add_product_page'),
    url(r'^add_product$', views.add_product_to_db, name = 'manage_products_add_product'),
    url(r'^edit_product_page/(?P<id>\d+)$', views.edit_product_page, name = 'manage_products_edit_product_page'),
    url(r'^edit_product$', views.edit_product, name = 'manage_products_edit_product'),
    url(r'^delete_product$', views.delete_product_from_db, name = 'manage_products_delete_product'),
]