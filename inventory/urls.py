"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inve import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_login', views.admin_login),
    path('admin_register', views.admin_register),
    path('admin_home', views.admin_home),
    path('add_staff', views.add_staff),
    path('manage_staff', views.manage_staff),
    path('search_staff', views.search_staff),
    path('edit_staff/<int:id>', views.edit_staff),
    path('edi_staff_save', views.edi_staff_save),
    path('add_supplier', views.add_supplier),
    path('manage_supplier', views.manage_supplier),
    path('search_supplier', views.search_supplier),
    path('add_product', views.add_product),
    path('manage_product', views.manage_product),
    path('search_product', views.search_product),
    path('order', views.order),
    path('delivery', views.delivery),
    path('admin_logout', views.admin_logout)
]
