from django.urls import path, include
from blockchain import views

urlpatterns = [
    path('', views.MainView.as_view(), name = 'homepage'),
    path('blockview/<int:id>', views.block_view, name = 'blockview')
]
