"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="Homepage"),
    path('fundname/',views.fundnames,name="fundnames"),
    path('getNav',views.getNav,name="Get Nav"),
    path('bestMF',views.getBestMF,name="getBestMF"),
    path('future_nav',views.future_nav,name="Get Future Nav Predition"),
    path('past_nav',views.ReadCsv,name="Previous Data"),
    path('all_future_nav',views.all_future_nav,name="All Future Nav Data"),
    path('bestMFMerged',views.bestMFMerged,name="Predict Best MF")
]
