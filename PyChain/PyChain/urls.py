from django.urls import path
from blockchain import views

urlpatterns = [
    path('mine_block/', views.MineBlock.as_view(), name='mine_block'),
    path('get_chain/', views.GetChain.as_view(), name='get_chain'),
    path('is_valid/', views.IsValid.as_view(), name='is_valid'),
]
