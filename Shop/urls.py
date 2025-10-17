from django.urls import path
from .import views
urlpatterns = [
    path("", views.home, name='home'),
    path("signup/", views.registerpage, name='signup'),
    path("login/", views.loginpage, name='login'),
    path("logout/", views.logoutpage, name='logout'),
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name="cart"),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('remove-cart-item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('cart/update/<int:product_id>/<str:action>/', views.update_item_quantity, name='update_item_quantity'),
    path('checkout/', views.checkout, name="checkout"),
    path('order-confirm/', views.confirm_order, name="confirm_order"),
    path('my-orders/', views.my_orders, name='my_orders')
]