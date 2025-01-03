from django.shortcuts import render,redirect
from .models import Products,Order
from django.core.paginator import Paginator
import json
# Create your views here.


def index(request):
    product_object = Products.objects.all()
    
    item_name = request.GET.get('item_name')
    
    if item_name :
        product_object = Products.objects.filter(title__icontains=item_name)
        
    #paginator
    paginator = Paginator(product_object,10)   
    page = request.GET.get('page')
    product_object =paginator.get_page(page)
        
    return render(request, 'shop/index.html',{'product_object':product_object})



def detail(request,id):
    product_object = Products.objects.get(id=id)
    
    
    return render(request, 'shop/detail.html',{'product_object':product_object})

def checkout(request):
    # Initialize variables for both GET and POST requests
    name = ''
    email = ''
    city = ''
    state = ''
    zip_code = ''
    contact = ''

    if request.method == 'POST':
        # Extract data from the form if the request method is POST
        items =request.POST.get('items',"")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zip_code = request.POST.get('zip', "")
        contact = request.POST.get('contact', "")
   
        # Save the order to the database
        order = Order(items=items,name=name, email=email, city=city, state=state, zip_code=zip_code, contact=contact)
        order.save()

    return render(request, 'shop/checkout.html', {
        'name': name, 'email': email, 'city': city, 'state': state, 'zip_code': zip_code, 'contact': contact
    })
