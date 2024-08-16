from django.urls import path 

from . import views

urlpatterns = [
    path('menu-items', views.MenuItemView.as_view(), name="menu_item_view"),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name="single_menu_item_view"),
    path('menu-items/category', views.CategoryView.as_view(), name="category_view"),
    path('groups/managers/users', views.ManagerView.as_view(), name="manager_view"),
    path('groups/managers/users/<int:pk>', views.ManagerRemoveView.as_view(), name="manager_remove_view"),
    path('groups/delivery-crew/users', views.DeliveryCrewView.as_view(), name="delivery_crew_view"),
    path('groups/delivery-crew/users/<int:pk>', views.DeliveryCrewRemoveView.as_view(), name="deliver_crew_remove"),
    path('cart/menu-items', views.CartView.as_view(), name="cart_menuitems"),
    path('orders', views.OrderView.as_view(), name="order_view"),
    path('orders/<int:pk>', views.SingleOrderView.as_view(), name="single_order_view"),
]