from django.urls import path
from . import views

urlpatterns=[
  path('',views.home),
  path('login/',views.login, name='login'),
  path('signup/', views.register, name='signup'),
  path('todolist/', views.addtask, name='todolist'),
  path('updatetask/', views.updatetask, name='updatetask'),
  path('viewtask/', views.viewtask, name='viewtask'),
  path('contact/', views.contact, name='contact'),
]