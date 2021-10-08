from django.urls import path
# from .views import WalletCreateAPIView
from . import views

app_name = 'wallet'

urlpatterns = [
    path('create_wallet',views.create_wallet, name='create_wallet'),
    path('create_wallet_api',views.create_wallet_api, name='create_wallet_api'),
    path('add_money_to_wallet/<int:pk>',views.add_money, name='add_money'),
    path('currentid/',views.sample_view, name='id'),
    path('currentwallet/',views.sample_wallet_view, name='walletid'),
    path('check_balance/<int:pk>',views.check_balance, name='checkbalance'),
    path('delete_wallet/<int:pk>',views.delete_wallet, name='deletewallet'),

]