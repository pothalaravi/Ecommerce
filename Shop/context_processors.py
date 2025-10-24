from .models import Customer

def login_user(request):
    customer_id = request.session.get('customer_id')
    user = None
    if customer_id:
        try:
            user = Customer.objects.get(id=customer_id)
        except:
            user = None
    return {'login_user': user}
