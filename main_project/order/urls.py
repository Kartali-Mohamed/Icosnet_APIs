from django.urls import path
from . import views

urlpatterns = [
    path('order/create/' , views.create_an_order),
    path('order/' , views.get_orders),
    path('order/<str:pk>/' , views.get_order_by_id),
    path('search/order/' , views.get_search_orders),
    path('order/update/<str:pk>/' , views.update_order),
    path('order/cancel/<str:pk>/' , views.cancel_order),
]