from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from items.models import Item

from .forms import DiscourseMessageForm
from .models import Discourse


@login_required
def new_discourse(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if item.created_by == request.user:
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))

    discourses = Discourse.objects.filter(item=item).filter(
        members__in=[request.user.id]
    )
    if discourses:
        return redirect("discourse:detail", discourse_id=discourses.first().id)

    if request.method == "POST":
        form = DiscourseMessageForm(request.POST)
        if form.is_valid():
            discourse = Discourse.objects.create(item_id=item_id)
            discourse.members.add(request.user)
            discourse.members.add(item.created_by)

            message = form.save(commit=False)
            message.discourse = discourse
            message.created_by = request.user
            message.save()
            return redirect("items:item_detail", item_id=item_id)
    else:
        form = DiscourseMessageForm()
    return render(request, "discourse/new.html", {"form": form})


@login_required
def inbox(request):
    discourses = Discourse.objects.filter(members__in=[request.user.id])
    return render(request, "discourse/inbox.html", {"discourses": discourses})


@login_required
def detail(request, discourse_id):
    discourse = get_object_or_404(
        Discourse, pk=discourse_id, members__in=[request.user.id]
    )

    if request.method == "POST":
        form = DiscourseMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.discourse = discourse
            message.created_by = request.user
            message.save()
            discourse.save()
            return redirect("discourse:detail", discourse_id=discourse_id)
        else:
            print(form.errors)
    else:
        form = DiscourseMessageForm()
    return render(
        request, "discourse/detail.html", {"discourse": discourse, "form": form}
    )
