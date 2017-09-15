from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'admin_index'),
    url(r'^login$', views.login, name = 'admin_login'),
    url(r'^register_admin$', views.register_admin, name = 'admin_register_admin'),
    url(r'^mission_control$', views.mission_control, name = 'admin_mission_control'),
    url(r'^logout$', views.logout, name = 'admin_logout'),
    url(r'^users$', views.edit_users, name = 'admin_users'),
    url(r'^products$', views.edit_products, name = 'admin_products'),
    url(r'^delete_admin$', views.delete_admin, name = 'admin_delete_admin'),
    url(r'^edit_admin_page/(?P<id>\d+)$', views.edit_admin_page, name = 'admin_edit_admin_page'),
    url(r'^edit_admin', views.edit_admin, name = 'admin_edit_admin'),
]