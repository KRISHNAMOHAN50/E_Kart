from django.shortcuts import render
import store.models 



def home(request):
    products = store.models.Product.objects.all().filter(is_avilable=True)

    context = {
        'products': products,
    }

    return render(request,'home.html', context) 