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
from .models import Payment
from django.http import HttpResponse
from .models import Slider
import json
import requests
@login_required
def verify_order(request):
    # Add your logic to verify the Khalti order
    return HttpResponse('Order verification successful')
@login_required
def home(request):
    sliders = Slider.objects.all()

    totalitem =0 
    wishitem =0
    if request.user.is_authenticated:
               totalitem =len(Cart.objects.filter(user=request.user))
               wishitem =len(Wishlist.objects.filter(user=request.user))
    return render(request,'home.html',{'sliders': sliders})
   
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
               cart_items =Cart.objects.filter(user=user)
               famount =0
               for p in cart_items:
                value =p.quantity* p.product.discounted_price
                famount =famount+value
                totalamount =famount+40
                return render(request,'checkout.html',locals())  
     

@login_required
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()

        cart = Cart.objects.filter(user=request.user)
        amount = sum(item.quantity * item.product.discounted_price for item in cart)

        total_amount = amount + 40

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': total_amount
        }

        return JsonResponse(data)



@login_required
def minus_cart(request):
    if request.method == 'GET':
         prod_id = request.GET.get('prod_id') # Use get() method instead of indexing
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity -= 1
    c.save()
    user = request.user
    cart =Cart.objects.filter(user=user)
    amount =0
    for p in cart:
         value = p.quantity*p.product.discounted_price
         amount =amount+value

    totalamount =amount+40

    data = {
      'quantity': c.quantity,
      'amount': amount,
      'totalamount': totalamount
    }
    return JsonResponse(data) 
    
@login_required
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        cart_item = Cart.objects.filter(Q(product=prod_id) & Q(user=request.user)).first()
        if cart_item:
            cart_item.delete()

        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = sum(item.quantity * item.product.discounted_price for item in cart)
        total_amount = amount + 40

        data = {
            'amount': amount,
            'totalamount': total_amount
        }

        return JsonResponse(data)
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
    return redirect('cart')


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
    wishitem = 0
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    orderPlaced = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'orders.html', locals())


@login_required
def payment_done(request):
    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    cust_id = request.GET.get('cust_id')
    user = request.user
    customer = Customer.objects.get(id=cust_id)
    cart = Cart.objects.filter(user=user)
    amount = 1000  # Update the amount as needed
    return redirect("orders")


@login_required
def verify_payment(request):
    data = request.POST
    product_id = data['product_identity']
    token = data['token']
    amount = data['amount']

    url = "https://khalti.com/api/v2/payment/verify/"
    payload = {
        "token": token,
        "amount": amount
    }
    headers = {
        "Authorization": "Key test_secret_key_614eec0ede624202b701d4fc638ec86c"
    }

    response = requests.post(url, data=payload, headers=headers)
    response_data = json.loads(response.text)
    status_code = str(response.status_code)

    if status_code == '400':
        response = JsonResponse({'status': 'false', 'message': response_data['detail']}, status=500)
        return response

    return JsonResponse(f"Payment Done !! With IDX. {response_data['user']['idx']}", safe=False)
