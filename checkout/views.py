from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OXAoLAG5VMJODD2HddnY1ooccK8T9ZbOVk1Lp1GIk0aOs9E9E0t1tjZU1xBn3j81ifU1A0D68DCkGoxnbxrncme00EkECoID1',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)