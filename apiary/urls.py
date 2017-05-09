"""apiary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from apiary.views import index, GroupView
from apiary.views import NetworkView, NodeView, SensorView, FeatureView, UserView

router = DefaultRouter()
router.register(r'networks', NetworkView)
router.register(r'nodes', NodeView)
router.register(r'sensors', SensorView)
router.register(r'features', FeatureView)
router.register(r'users', UserView)
router.register(r'groups', GroupView)

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls)
]
