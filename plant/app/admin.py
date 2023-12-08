from django.contrib import admin
from . models import Product,Customer,Cart,Payment,OrderPlaced, ReviewRating,Wishlist,Slider
# Register your models here.
@admin.register(Slider)
class SliderModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'details')
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display =['id','title','discounted_price','category','product_image']
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display =['id','user','address']
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display =['id','user','product','quantity']

class WishlistAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product']  

admin.site.register(ReviewRating)