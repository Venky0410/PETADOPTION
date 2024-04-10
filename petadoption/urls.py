from django.contrib import admin
from django.urls import include, path
 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('petadoption/', include('petadoption.urls')),  # Include petadoption app URLs
]
"""
from django.contrib import admin
from .views import dashboard, admin_dashboard
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),
    # path('admin/', admin.site.urls),
    # path('petadoption/', include('petadoption.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  
    # path('cats/', views.cats, name='cats'),
    path('animals_list/', views.animals_list, name='animals_list'),
    # path('rabbits/', views.rabbits, name='rabbits'),
    path('animal-detail/<int:animal_id>/', views.animal_detail, name='animal_detail'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('user-login/', views.user_login, name='user_login'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add-animal/', views.add_animal, name='add_animal'),
    path('edit-animal/<int:animal_id>/', views.edit_animal, name='edit_animal'),
    path('delete-animal/<int:animal_id>/', views.delete_animal, name='delete_animal'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
