from django.conf.urls import url, re_path

from . import views

urlpatterns = [
    re_path(r'items/', views.items, name='item'),
    re_path(r'^upadate-item/$', views.edit_item, name='edit_item'),
]
