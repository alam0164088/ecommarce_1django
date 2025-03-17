from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category

def home(request):
    # ক্যাটাগরি অনুযায়ী প্রোডাক্ট ফিল্টার
    laptops = Product.objects.filter(category__name='Laptop')[:4]
    phones = Product.objects.filter(category__name='Phone')[:4]
    others = Product.objects.exclude(category__name__in=['Laptop', 'Phone'])[:4]
    
    return render(request, 'store/home.html', {
        'laptops': laptops,
        'phones': phones,
        'others': others
    })

def product_list(request):
    products = Product.objects.all()  # সব প্রোডাক্ট
    return render(request, 'store/products.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST' and 'add_to_cart' in request.POST:
        cart = request.session.get('cart', {})
        cart[str(product.pk)] = cart.get(str(product.pk), 0) + 1
        request.session['cart'] = cart
        return redirect('cart')
    return render(request, 'store/product_detail.html', {'product': product})

def about(request):
    return render(request, 'store/about.html')

def contact(request):
    return render(request, 'store/contact.html')

def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        total = product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': total
        })
        total_price += total
    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

def search(request):
    query = request.GET.get('q')  # প্রোডাক্ট নাম
    min_price = request.GET.get('min_price')  # মিনিমাম প্রাইস
    max_price = request.GET.get('max_price')  # ম্যাক্সিমাম প্রাইস

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    return render(request, 'store/search_results.html', {
        'products': products,
        'query': query,
        'min_price': min_price,
        'max_price': max_price
    })


