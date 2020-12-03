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
        'stripe_public_key': 'pk_test_51HuNpFDLeDN6RAorKOp3WPo6Thq1axUedpa7TAhDTJFgqGcV1kZCvH8L37YTCfieR6xul3FFzJZHARZNuLqai8hn005EaZSQ9o',
        'client_secret': 'sk_test_51HuNpFDLeDN6RAorIUz2iVVUXMMokqsONDE2Bj4jrTftgSIzm57idROFIS9I2K2YuXW1NNhJTFR5y1CyEToEraWI00pMWvBohG',
    }

    return render(request, template, context)