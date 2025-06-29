from django.shortcuts import get_object_or_404, render

from .models import Item


def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(
        pk=item_id
    )[:3]
    return render(
        request, "item/detail.html", {"item": item, "related_items": related_items}
    )
