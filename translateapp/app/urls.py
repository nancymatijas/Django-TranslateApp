from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path('accept_bid/<int:bid_id>/', views.accept_bid, name='accept_bid'),

]
