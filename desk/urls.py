from django import views
from django.urls import path
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('complain', Complain_data, name='complain'),
    path('insert_complain', login_required(login_url='login')(views.Insert_complain.as_view()), name='insert_complain'),
    path('delete_complain/<int:id>', Delete_complain, name='delete_complain'),
    path('insert_feedback', login_required(login_url='login')(views.Insert_feedback.as_view()), name='insert_feedback'),
    path('delete_feedback/<int:id>', Delete_feedback, name='delete_feedback'),
    path('student', Student_data, name='student'),
    path('feedback', Feed_data, name='feedback'),
    path('login', Login, name='login'),
    path('signup', Signup, name='signup'),
    path('validate', validate, name='validate'),
    path('', Dashboard, name='dashboard'),
    path('about',Aboutus,name='about'),
    path('logout', Logout, name='logout'),
    path('insert_student', Insert_student.as_view(), name='insert_student'),
    path('main',AdminSide,name='main')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
