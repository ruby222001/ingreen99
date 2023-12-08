from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.urls import include, path

from . import views
from .forms import LoginForm, MyPasswordResetForm

urlpatterns = [
    path("", views.home,name='home'),
    path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
    path("product-detail/<int:pk>",views.ProductDetail.as_view(), name="product-detail"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path("category.title/<val>",views.CategoryTitle.as_view(),name="category-title"),
    path('profile/',views.ProfileView.as_view(),name='profile'),

    path('address/',views.address,name='address'),
    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('showcart/',views.show_cart,name='showcart'),

    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
path('removecart/', views.remove_cart, name='remove-cart'),
    path('cart/', views.show_cart, name='cart'),
    path('add-to-cart-from-wishlist/<int:item_id>/', views.add_to_cart_from_wishlist, name='add-to-cart-from-wishlist'),
 path('wishlist/', views.Wishlist, name='wishlist'),
path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),

    path('search/',views.search,name='search'),
    path('orders/',views.home,name='orders'),
path('updateaddress/<int:pk>',views.updateAddress.as_view(),name='updateaddress'),
    path('registration/',views.CustomerRegistrationview.as_view(),name='customerregistration'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='login.html',authentication_form = LoginForm),name='login'),
      path('logout/',auth_view.LogoutView.as_view(),name='logout'),
path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
path('checkout/', views.CheckoutView.as_view(), name='checkout'),
 path('verify_payment/',views.verify_payment,name='verify_payment'),
 path('payment/',views.payment,name='payment'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
admin.site.site_header="ingreen"
admin.site.site_title="ingreen"
admin.site.site_index_title="Welcome to ingreen"