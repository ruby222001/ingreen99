from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordResetForm
urlpatterns = [
    path("", views.home),
    path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
    path("product-detail/<int:pk>",
         views.ProductDetail.as_view(), name="product-detail"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path("category.title/<val>",views.CategoryTitle.as_view(),name="category-title"),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/',views.address,name='address'),
    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('showcart/',views.show_cart,name='showcart'),
path('checkout/', views.checkoutView.as_view(), name='checkout'),

    path('pluscart/', views.plus_cart, name='plus-cart'),
    path('minuscart/', views.minus_cart, name='minus-cart'),
    path('removecart/', views.remove_cart, name='remove-cart'),
    # ...
 
    # ...
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add-to-cart-from-wishlist/<int:item_id>/', views.add_to_cart_from_wishlist, name='add-to-cart-from-wishlist'),


 
    path('search/',views.search,name='search'),
    path('orders/',views.home,name='orders'),

    path('paymentdone/',views.payment_done,name='paymentdone'),
path('updateaddress/<int:pk>',views.updateAddress.as_view(),name='updateaddress'),
    path('registration/',views.CustomerRegistrationview.as_view(),name='customerregistration'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='login.html',authentication_form = LoginForm),name='login'),
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='changepassword.html',form_class=MyPasswordResetForm,success_url='/passwordchangedone'),name='passwordchange'),
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='password_reset.html',form_class =MyPasswordResetForm),name='password_reset'),
   path('passwordchangedone/' ,auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header="ingreen99"
admin.site.site_title="ingreen99"
admin.site.site_index_title="Welcome to ingreen99"