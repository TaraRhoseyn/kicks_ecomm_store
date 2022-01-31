from django.conf import settings
from decimal import Decimal

# Makes dict available to all apps
def bag_items(request):

    bag_item_li = []
    total = 0
    product_nu = 0
    grand_total = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        grand_total = total + Decimal(settings.DELIVERY_COST)
    else:
        grand_total = total
        print("not enough")
        # insert code to let user know how much more to spend to get free deliv

    context = {
        'bag_item_li': bag_items_li,
        'total': total,
        'product_nu': product_nu,
        'grand_total', grand_total,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
    }

    return context
