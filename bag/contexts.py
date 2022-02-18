# IMPORTS 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Third party
from django.conf import settings
from django.shortcuts import get_object_or_404
from decimal import Decimal

# Internal
from products.models import Product

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def bag_items(request):
    """
    A context that contains the bag contents
    and makes it available to all apps
    Args:
        request (object): HTTP request object
    Returns:
        Context object containing bag items
    """
    bag_items = []
    total = 0
    product_count = 0
    delivery = Decimal(settings.DELIVERY_COST)
    bag = request.session.get('bag', {})

    # Credit: Code Institute
    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        grand_total = total + delivery
        free_delivery_delta = Decimal(settings.FREE_DELIVERY_THRESHOLD) - total
    else:
        delivery = 0
        free_delivery_delta = 0
        grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'product_count': product_count,
        'grand_total': grand_total,
        'product_count': product_count,
        'free_delivery_threshold': Decimal(settings.FREE_DELIVERY_THRESHOLD),
    }

    return context
