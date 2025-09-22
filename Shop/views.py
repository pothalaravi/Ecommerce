from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Product, Category, Customer
from django.contrib.auth.hashers import make_password, check_password

def home(request):
    categories = Category.objects.all()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_category_id(categoryID)
    else:
        products = Product.objects.all()
    data = {'products': products, 'categories': categories}
    return render(request, 'index.html', data)


# ===== Signup View =====
def Signup(request):
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
    




def Login(request):
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
                return redirect('home')
            else:
                error_msg = "password id incorrect"
                msg ={'error':error_msg}
                return render(request, 'login.html', msg)
    
        else:
            error_msg = "Email is incorrect"
            msg ={'error':error_msg}
            return render(request, 'login.html', msg)
        


def Logout(request):
    return redirect("login")

        
    