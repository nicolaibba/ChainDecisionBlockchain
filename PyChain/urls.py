from django.urls import path, include
from django.contrib import admin
from blockchain import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blockchain.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
