from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Cart, Product, Category, Customer
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.hashers import make_password, check_password

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    categoryID = request.GET.get('category')
    search = request.GET.get('search')
    # sort = request.GET.grt('sort')
    if categoryID:
        products = Product.get_category_id(categoryID)
    if search:
        products = Product.objects.filter(name__icontains=search)
    else:
        products = Product.objects.all()
        # print(products)
    customer_id=request.session.get('customer_id')
    cart_item_count=0
    if customer_id:
        cart_item_count=Cart.objects.filter(customer_id=customer_id).count()
    data = {'products': products, 'categories': categories, 'cart_item_count':cart_item_count}
    
    return render(request, 'index.html', data)


# ===== Signup View =====
def Registerpage(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    else:
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        password = make_password(password)
        userdata = [full_name,email,mobile,password]
        print(userdata)
        uservalues={
            'full_name':full_name,
            'email':email,
            'mobile':mobile
        }
        
        customerdata =Customer(full_name=full_name, email=email, mobile=mobile,password=password)


        error_msg = None
        success_msg = None

    
        if(not full_name):
            error_msg = "Full name is required"
        elif(not email):
            error_msg = "Email is required"
        elif(not mobile):
            error_msg = "Mobile number is required"
        elif(not password):
            error_msg = "Password is required"
        elif(customerdata.isexist()):
            error_msg="Email Alredy Exists"
        if (not error_msg):
            success_msg="Account Created Successfully"
            customerdata.save()
            msg={'success':success_msg}
            return render(request, 'signup.html', msg)
        else:
            msg ={'error':error_msg,  'values':uservalues}
            return render(request, 'signup.html', msg)
    




def Loginpage(request):
    if request.method=='GET':
        return render(request, 'login.html')
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')


        users= Customer.isexist(email)
        error_msg = None
        if users:
            check = check_password(password, users.password)
            if check:
                request.session['customer_id'] = users.id
                request.session['customer_email'] = users.email
                return redirect('home')
            else:
                error_msg = "password id incorrect"
                msg ={'error':error_msg}
                return render(request, 'login.html', msg)
    
        else:
            error_msg = "Email is incorrect"
        msg ={'error':error_msg}
        return render(request, 'login.html', msg)
        


def Logoutpage(request):
    auth_logout(request)
    messages.success(request, " Logout Successfully ")
    return redirect("login")


def add_to_cart(request, product_id):
    customer_id =request.session.get('customer_id')
    if not customer_id:
        return redirect('login')
    
    customer = get_object_or_404(Customer,  id=customer_id)
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = Cart.objects.get_or_create(customer=customer, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')
    # cart = request.session.get('cart', {})
    # product_id = str(product_id)
    # if product_id in cart:
    #     cart[product_id] += 1
    # else:
    #     cart[product_id] = 1

    # request.session['cart'] = cart

    # return redirect ('home')


# def show_cart(request):
#     cart = request.session.get('cart', {})
#     products = []
#     total = 0


#     for product_id, quantity in cart.items():
#         product = Product.objects.get(id=product_id)
#         product.quantity = quantity
#         product.total_price = product.price * quantity
#         products.append(product)
#         total += product.total_price

#     return render(request, 'cart.html', {'products': products, 'total': total})

def cart(request):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('login')
    
    customer = get_object_or_404(Customer, id=customer_id)
    cart_items = Cart.objects.filter(customer=customer)

    total = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'cart.html', {'products': cart_items, 'total': total})



def product_detail(request, product_id):
    product = get_object_or_404(Product, id =product_id)
    return render(request, 'product_detail.html', {'product':product})


def remove_cart_item(request, product_id):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('login')
    
    cart_item = Cart.objects.filter(customer=customer_id, product_id=product_id)
    cart_item.delete()
    return redirect('cart')

def update_item_quantity(request, product_id, action):
    customer_id = request.session.get('customer_id')
    customer = get_object_or_404(Customer, id=customer_id)
    cart_item = get_object_or_404(Cart, customer=customer, product_id=product_id)
    if action == 'increase':
        cart_item.quantity += 1

    elif action == 'decrease' and  cart_item.quantity > 1:
        cart_item.quantity -= 1
    cart_item.save()
    return redirect ('cart')

        



    