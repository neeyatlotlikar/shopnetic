from django import forms

from .models import DiscourseMessage


class DiscourseMessageForm(forms.ModelForm):
    class Meta:
        model = DiscourseMessage
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Type your message here...",
                       "class": "w-full px-6 py-4 rounded-xl border"}
            ),
        }
