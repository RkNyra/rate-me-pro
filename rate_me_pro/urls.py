"""rate_me_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views
from django_registration.backends.one_step.views import RegistrationView
from rest_framework import routers
from rates.views import UserViewSet, GroupViewSet, ProjectViewSet, ProfileViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'profiles', ProfileViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rates.urls')),
    path('accounts/register/',RegistrationView.as_view(success_url='/accounts/login/')),
    path('accounts/',include('django_registration.backends.one_step.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout/',views.LogoutView.as_view(),{'next_page':'/'}),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token)
]
