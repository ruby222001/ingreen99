from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views import View
from .models import Product,Customer,Cart,OrderPlaced,Payment,Wishlist
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Slider


@login_required
def home(request):
     totalitem =0 
     wishitem =0
     if request.user.is_authenticated:
               totalitem =len(Cart.objects.filter(user=request.user))
               wishitem =len(Wishlist.objects.filter(user=request.user))
     return render(request,'home.html')
   
@login_required
def about(request):
     totalitem =0 
     wishitem =0
     if request.user.is_authenticated:
               totalitem =len(Cart.objects.filter(user=request.user))
               wishitem =len(Wishlist.objects.filter(user=request.user))
     return render(request,"about.html")
@login_required
def contact(request):
     totalitem =0 
     wishitem =0
     if request.user.is_authenticated:
               totalitem =len(Cart.objects.filter(user=request.user))
               wishitem =len(Wishlist.objects.filter(user=request.user))
     return render(request,"contact.html")

@method_decorator(login_required,name='dispatch')
class CategoryView(View):
    def get(self,request,val):
     totalitem =0 
     wishitem =0
     if request.user.is_authenticated:
               totalitem =len(Cart.objects.filter(user=request.user))
               wishitem =len(Wishlist.objects.filter(user=request.user))
     product =Product.objects.filter(category=val)
     title =Product.objects.filter(category=val).values('title') 
     return render(request,"category.html",locals())
    
@method_decorator(login_required,name='dispatch')
class CategoryTitle(View ):
    def get(self,request,val):
        product =Product.objects.filter(title =val)
        title =Product.objects.filter(category =product[0].category).values('title') 
        wishitem =0
        totalitem =0 
        if request.user.is_authenticated:
               totalitem =len(Cart.objects.filter(user=request.user))
               wishitem =len(Wishlist.objects.filter(user=request.user))
        return render(request,"category.html",locals())
    
@method_decorator(login_required,name='dispatch')
class ProductDetail(View):
     def get(self,request,pk):
          product=Product.objects.get(pk=pk)
          wishlist = Wishlist.objects.filter(Q(product=product)&Q(user=request.user))
          wishitem =0
          totalitem =0 
          if request.user.is_authenticated:
               totalitem =len(Cart.objects.filter(user=request.user))
               wishitem =len(Wishlist.objects.filter(user=request.user))
          return render(request,"productdetail.html",locals())
     
@method_decorator(login_required,name='dispatch')
class CustomerRegistrationview(View):
     def get(self,request):
          form =CustomerRegistrationForm()
          wishitem =0
          totalitem =0 
          if request.user.is_authenticated:
               totalitem =len(Cart.objects.filter(user=request.user))
               wishitem =len(Wishlist.objects.filter(user=request.user))
          return render(request,'customerregistration.html',locals())
     def post(self,request):
          form =CustomerRegistrationForm(request.POST)
          if form.is_valid():
               form.save()
               messages.success(request,"user register successfull")
          else:
               messages.warning(request,"invalid input data")
          return render(request,'customerregistration.html',locals())
     
@method_decorator(login_required,name='dispatch')
class ProfileView(View):
     def get(self,request):
          form =CustomerProfileForm()
          wishitem =0
          totalitem =0 
          if request.user.is_authenticated:
               totalitem =len(Cart.objects.filter(user=request.user))
               wishitem =len(Wishlist.objects.filter(user=request.user))
          return render(request,'profile.html',locals())
     def post(self,request):
          form =CustomerProfileForm(request.POST)
          if form.is_valid():
               user = request.user
               name = form.cleaned_data['name']

               address = form.cleaned_data['address']
               mobile=form.cleaned_data['mobile']
               reg = Customer(user=user,name=name,address=address,mobile=mobile)
               reg.save()
               messages.success(request,"Congratulations! profile saved Successfully")
          else:
               messages.warning(request,"invalid Input Data")
          return render(request,'profile.html',locals())

@login_required
def address(request):
     add = Customer.objects.filter(user=request.user)
     wishitem =0
     totalitem =0 
     if request.user.is_authenticated:
               totalitem =len(Cart.objects.filter(user=request.user))
               wishitem =len(Wishlist.objects.filter(user=request.user))
          
     return render(request,'address.html',locals())

@method_decorator(login_required,name='dispatch')    
class updateAddress(View):
     def get(self,request,pk):
          add = Customer.objects.get(pk=pk)
          form = CustomerProfileForm()
          wishitem =0
          totalitem =0 
          if request.user.is_authenticated:
               totalitem =len(Cart.objects.filter(user=request.user))
               wishitem =len(Wishlist.objects.filter(user=request.user))
          
          return render(request,'updateaddress.html',locals())
     def post(self,request,pk):
           form = CustomerProfileForm(request.POST)
           if form.is_valid():
                add= Customer.objects.get(pk=pk)
                add.name =form.cleaned_data['name']
                add.mobile = form.cleaned_data['mobile']
                add.save()
                messages.success(request,"Congratulation ! Profile update Successfull")
           else:
                messages.warning(request,"Invalid Input Data")
           return redirect("address")
     
@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    if 'next' in request.GET:
        return redirect(request.GET.get('next'))
    return redirect('showcart')

@login_required
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount += value
    totalamount = amount + 40
    wishitem = 0
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))

    return render(request, 'addtocart.html', locals())

@method_decorator(login_required,name='dispatch')
class checkoutView(View):
    def get(self,request):
     wishitem =0
     totalitem =0 
     if request.user.is_authenticated:
               totalitem =len(Cart.objects.filter(user=request.user))
               wishitem =len(Wishlist.objects.filter(user=request.user))  
     user =request.user
     add=Customer.objects.filter(user=user)
     cart =Cart.objects.filter(user=user)
     famount =0
     for p in cart:
          value =p.quantity* p.product.discounted_price
          famount =famount+value
     totalamount =famount+40
     return render(request,'checkout.html',locals())

@login_required
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        cart_item = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        cart_item.quantity += 1
        cart_item.save()

        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount += value
        totalamount = amount + 40

        data = {
            'quantity': cart_item.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)

@login_required
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        cart_item = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()

        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount += value
        totalamount = amount + 40

        data = {
            'quantity': cart_item.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)

@login_required
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        cart_item = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        cart_item.delete()

        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount += value
        totalamount = amount + 40

        data = {
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Wishlist, Cart

@login_required
def wishlist(request):
    user = request.user
    wishlist_items = Wishlist.objects.filter(user=user)
    context = {
        'wishlist_items': wishlist_items,
    }
    return render(request, 'wishlist.html', context)

@login_required
def add_to_cart_from_wishlist(request, item_id):
    wishlist_item = Wishlist.objects.get(id=item_id)
    product = wishlist_item.product
    Cart(user=request.user, product=product).save()
    wishlist_item.delete()
    return redirect('showcart')



@login_required
def search(request):
    query = request.GET.get('search')
    wishitem = 0
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    product = Product.objects.filter(title__icontains=query)
    return render(request, "search.html", {'product': product, 'wishitem': wishitem, 'totalitem': totalitem})
@login_required
def orders(request):
     wishitem =0
     totalitem =0 
     if request.user.is_authenticated:
               totalitem =len(Cart.objects.filter(user=request.user))
               wishitem =len(Wishlist.objects.filter(user=request.user))
     orderPlaced=OrderPlaced.objects.filter(user=request.user)
     return render(request,'orders.html',locals())
@login_required
def payment_done(request):
     order_id = request.GET.get('order_id')
     payment_id =request.GET.get('payment_id')
     cust_id=request.GET.get('cust_id')
     user =request.user
     customer =Customer.objects.get(id=cust_id)
     payment =Payment.objects.get()
     cart= Cart.objects.filter(user=user)
     for c in cart:
          OrderPlaced(user=user ,customer=customer,product=c.product,quantity=c.quantity,payment=payment).save()
          c.delete()
     return redirect("orders")