from django.contrib import admin
from . models import Product,Customer,Cart,Payment,OrderPlaced,Wishlist,Slider

# Register your models here.
class SliderModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Slider
        list_display = ('title', 'image', 'description')
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display =['id','title','discounted_price','category','product_image']


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display =['id','user','address']
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display =['id','user','product','quantity']
@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display =['id','user','amount']
@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordered_data','status','payment']

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display =['id','user']

