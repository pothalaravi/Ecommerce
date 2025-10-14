from django.urls import path
from .import views
urlpatterns = [
    path("", views.home, name='home'),
    path("signup/", views.Registerpage, name='signup'),
    path("login/", views.Loginpage, name='login'),
    path("logout/", views.Logoutpage, name='logout'),
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name="cart"),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('remove-cart-item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('cart/update/<int:product_id>/<str:action>/', views.update_item_quantity, name='update_item_quantity'),

]