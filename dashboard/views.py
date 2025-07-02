from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from items.models import Item


@login_required
def index(request):
    """
    View for the dashboard index page.

    It displays a list of all items created by the user
    in reverse chronological order.
    """
    items = Item.objects.filter(created_by=request.user).order_by("-created_at")
    return render(request, "dashboard/index.html", {"items": items})
