import logging
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

logger = logging.getLogger(__name__)

def product_list(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            logger.info("Тауар сәтті тіркелді: %s (ID=%s)", product.name, product.id)
            if product.is_low_stock:
                logger.warning("Қор азайды: %s (Қалдық: %s, Шек: %s)", product.name, product.quantity, product.min_stock)
            return redirect("product_list")
    else:
        form = ProductForm()

    products = Product.objects.all().order_by("-id")
    return render(request, "warehouse/index.html", {"form": form, "products": products})

def decrease_stock(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.quantity > 0:
        product.quantity -= 1
        product.save()
        if product.is_low_stock:
            logger.warning("Қор азайды: %s (Қалдық: %s, Шек: %s)", product.name, product.quantity, product.min_stock)
    return redirect("product_list")
