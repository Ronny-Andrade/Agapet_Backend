from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from pet.urls import router_mascota

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('mascota/', include('pet.urls')),
    path('vacuna/', include('vacuna.urls')),
    path('api/', include(router_mascota.urls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)