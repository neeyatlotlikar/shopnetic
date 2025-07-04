from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EditItemForm, NewItemForm
from .models import Category, Item


def items(request):
    query = request.GET.get("q", "")
    category_id = request.GET.get("category", 0)
    items = Item.objects.filter(is_sold=False).order_by("-created_at")
    categories = Category.objects.all()

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    if category_id:
        items = items.filter(category_id=category_id)

    return render(
        request,
        "item/items.html",
        {
            "items": items,
            "categories": categories,
            "query": query,
            "category_id": int(category_id),
        },
    )


def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(
        pk=item_id
    )[:3]
    return render(
        request, "item/detail.html", {"item": item, "related_items": related_items}
    )


@login_required
def new(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect("items:item_detail", item_id=item.id)
    else:
        form = NewItemForm()
    return render(request, "item/new.html", {"form": form, "title": "New Item"})


@login_required
def edit(request, item_id):
    item = get_object_or_404(Item, pk=item_id, created_by=request.user)
    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("items:item_detail", item_id=item_id)
    else:
        form = EditItemForm(instance=item)
    return render(request, "item/new.html", {"form": form, "title": "Edit Item"})


@login_required
def delete(request, item_id):
    item = get_object_or_404(Item, pk=item_id, created_by=request.user)
    item.delete()

    return redirect("dashboard:index")
