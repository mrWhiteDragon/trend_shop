from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.models import Cart
from .models import Order, OrderItem
from .forms import OrderForm


@login_required
def create_order(request):
    cart = get_object_or_404(Cart, customer=request.user)

    if request.method == 'POST':
        form = (OrderForm
                (request.POST))
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.cart = cart
            order.save()

            # Переносим товары из корзины в заказ
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )

            messages.success(request, "Ваш заказ успешно оформлен!")
            return redirect('orders:order_detail', order_id=order.id)
    else:
        initial = {
            'phone': request.user.phone,
            'email': request.user.email,
        }
        form = OrderForm(initial=initial)

    return render(request, 'orders/create_order.html', {
        'form': form,
        'cart': cart
    })


@login_required
def order_list(request):
    orders = Order.objects.filter(
        customer=request.user
    ).select_related('cart').prefetch_related('items').order_by('-created_at')

    return render(request, 'orders/order_list.html', {
        'orders': orders
    })


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(
        Order.objects.select_related('cart', 'customer')
        .prefetch_related('items__product'),
        id=order_id,
        customer=request.user
    )

    return render(request, 'orders/order_detail.html', {
        'order': order
    })


@login_required
def cancel_order(request, order_id):
    order = get_object_or_404(
        Order,
        id=order_id,
        customer=request.user,
        status='new'  # Можно отменять только новые заказы
    )

    order.status = 'cancelled'
    order.save()
    messages.success(request, f"Заказ {order.display_id} успешно отменён")
    return redirect('orders:order_detail', order_id=order.id)