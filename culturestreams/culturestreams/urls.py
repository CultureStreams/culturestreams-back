from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v0/', include('apiv00.urls')),
    path('api/v1/', include('apiv01.urls'))
]
