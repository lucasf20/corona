from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit', views.home_submit, name='home_submit'),
    path('fotoUp/',views.fotoUp, name= "fotoUp"),
    path('fotoUp/submit',views.fotoUp_submit, name= "fotoUp_submit"),
    path('resultado/',views.resultado, name= "resultado"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)