"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings  
from django.conf.urls.static import static  
from hotel.views import home,category,batafsil,single,delete,create,update,salom,alik,singlet
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('single/',single,name='single'),
    path('singlet/',singlet,name='singlet'),
    path('create/',create,name='create'),
    path('salom/',salom,name='salom'),
    path('alik/<int:id>/',alik,name='alik'),

    path('category/<int:id>/',category,name='category'),
    path('batafsil/<int:id>/',batafsil,name='batafsil'),
     path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',delete,name='delete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)