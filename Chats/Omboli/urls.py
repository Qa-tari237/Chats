from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib import admin

from . import views

#admin_site = Chatadmin(name='admin')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.omboli_frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('rooms/', views.rooms, name='rooms'),
    path('<slug:slug>/', views.room, name='room'),
]
