"""
URL configuration for ben_developer_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView

from portfolio import views as portfolio_views
from programs import views as programs_views

urlpatterns = [
    #path("", portfolio_views.index, name="index"),
    path('', TemplateView.as_view(template_name='portfolio/index.html'), name='index'),
    path("portfolio/index.html", portfolio_views.index, name="portfolio_index"),
    path("programs/", include("programs.urls")),
    path("admin/", admin.site.urls),
]
