from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    product_from_form = Product.objects.get(id=request.POST["product_id"])
    price_from_form = float(product_from_form.price)
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect('/order_confirm')

def order_confirm(request):
    all_orders = Order.objects.all()
    rolling_total = 0
    for order in all_orders:
        rolling_total += order.total_price
    context = {
        "last_order" : Order.objects.last(),
        "all_orders" : Order.objects.all(),
        "total_orders" : rolling_total,
    }
    return render(request,"store/checkout.html",context)