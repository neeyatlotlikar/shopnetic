from django import forms

from .models import Item

FORM_CLASSES = "w-full py-4 px-6 rounded-xl border"


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["category", "name", "description", "price", "image"]
        widgets = {
            "name": forms.TextInput(attrs={"class": FORM_CLASSES}),
            "description": forms.Textarea(attrs={"class": FORM_CLASSES}),
            "price": forms.NumberInput(attrs={"class": FORM_CLASSES}),
            "category": forms.Select(attrs={"class": FORM_CLASSES}),
            "image": forms.ClearableFileInput(attrs={"class": FORM_CLASSES}),
        }
        labels = {
            "name": "Item Name",
            "description": "Description",
            "price": "Price",
            "category": "Category",
            "image": "Item Image",
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["category", "name", "description", "price", "image", "is_sold"]
        widgets = {
            "name": forms.TextInput(attrs={"class": FORM_CLASSES}),
            "description": forms.Textarea(attrs={"class": FORM_CLASSES}),
            "price": forms.NumberInput(attrs={"class": FORM_CLASSES}),
            "category": forms.Select(attrs={"class": FORM_CLASSES}),
            "image": forms.ClearableFileInput(attrs={"class": FORM_CLASSES}),
            "is_sold": forms.CheckboxInput(attrs={"class": FORM_CLASSES}),
        }
        labels = {
            "name": "Item Name",
            "description": "Description",
            "price": "Price",
            "category": "Category",
            "image": "Item Image",
            "is_sold": "Sold Status",
        }
