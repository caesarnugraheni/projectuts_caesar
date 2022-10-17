from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('profil/', include('profil.urls')),
    path('visimisi/', include('visimisi.urls')),
    path('jadwal/', include('jadwal.urls')),
    path('materi/', include('materi.urls')),
    path('dosen/', include('dosen.urls')),
]
