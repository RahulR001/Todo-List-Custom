from django.urls import path
from . import views

urlpatterns=[
  path('',views.home),
  path('login/',views.login, name='login'),
  path('logout/',views.logout, name='logout'),
  path('signup/', views.register, name='signup'),
  path('todolist/', views.addtask, name='todolist'),
  path('update/', views.updatetask, name='update'),
  path('viewtask/', views.viewtask, name='viewtask'),
  path('contact/', views.contact, name='contact'),
]