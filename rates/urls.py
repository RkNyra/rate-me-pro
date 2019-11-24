from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    path('',views.index,name='index'),
    path('my-profile/',views.myProfile,name='my_profile'),
    path('submit-project/',views.submitProject,name='submit_project'),
]