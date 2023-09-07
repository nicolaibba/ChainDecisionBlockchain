from django.urls import path, include
from blockchain.views import MainView
from blockchain.blockviews import MineBlock, GetChain, IsValid

urlpatterns = [
    path('', MainView.as_view(), name = 'homepage'),
    path('mine_block/', MineBlock.as_view(), name='mine_block'),
    path('get_chain/', GetChain.as_view(), name='get_chain'),
    path('is_valid/', IsValid.as_view(), name='is_valid'),
    
    path('api-auth/', include('rest_framework.urls'))
]
