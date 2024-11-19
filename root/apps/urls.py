# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.home, name='home'),
# ]
from django.urls import path
from .views import register_view, login_view, logout_view, home_view, purchase
from . import views

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('purchase/<int:product_id>/', views.purchase, name='purchase')

]