from django.db import models
from django.contrib.auth.models import User
CATEGORY_CHOICES=(
    ('IP','indoorplant'),
    ('OP','outdoorplant'),
    ('RP','rareplant'),
    ('SP','succulents'),
    ('VP','variegatedplant'),
    ('CP','cactus'),
    ('PT','pots'),
    ('FT','fertilizer'),
)
# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slider')
    description = models.TextField()

    def __str__(self):
        return self.title
class Product(models.Model):
    title =models.CharField(max_length=100)
    selling_price =models.FloatField()
    discounted_price=models.FloatField()
    description =models.TextField()
    category =models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image =models.ImageField(upload_to='product')
    def __str__(self):
        return self.title

class Customer(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length =200)
    address =models.CharField(max_length=50)
    mobile =models.IntegerField(default=0)
    def __str__(self):
      return self.name
STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the Way','On the Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)

class Cart(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity =models.PositiveIntegerField(default=1)
    @property
    def total_cost(self):
      return self.quantity* self.product.discounted_price

class Payment(models.Model):
       user =models.ForeignKey(User,on_delete=models.CASCADE)
       amount =models.FloatField()
      
class OrderPlaced(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    customer =models.ForeignKey(Customer,on_delete=models.CASCADE)
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity =models.PositiveIntegerField(default=1)
    ordered_data=models.DateTimeField(auto_now_add=True)
    status =models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    payment =models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    @property
    def total_cost(self):
      return self.quantity* self.product.discounted_price
class Wishlist(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    product =models.ForeignKey(Product,on_delete=models.CASCADE)

