from django.shortcuts import render

from items.models import Category, Item


def index(request):
    """
    Render the index page.
    """
    # Fetch items and categories from the database
    items = Item.objects.filter(is_sold=False).order_by("-created_at")[0:10]
    categories = Category.objects.all()
    return render(
        request, "core/index.html", {"items": items, "categories": categories}
    )


def contact(request):
    """
    Render the contact page.
    """
    return render(request, "core/contact.html")
