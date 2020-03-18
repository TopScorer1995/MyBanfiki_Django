""" 
# Project Django Forms

Django forms can map HTML elements to Django model classes and provide data validation and automatic 
HTML widgets to represent model attributes.

The forms are instantiated in the application views and rendered in the project HTML template files. 
"""
"""
**Available Form Classes:**

1. ***ContactModelForm***: Form used to display and validate Contact Model instances.
2. ***InvoiceModelForm***: Form used to display and validate Invoice Model instances.
3. ***AccountModelForm***: Form used to display and validate Account Model instances.
4. ***TransactionModelForm***: Form used to display and validate Transaction Model instances.
5. ***InvoicePayForm***: Form used for Pay button on InvoiceListView..
6. ***InvoiceGenerateForm***: Form used to input the number of required automatically generated invoices.
"""

# === Imports ===

# Import Django modules
from django import forms
from django.forms import HiddenInput
from django.contrib.admin import widgets
from django.core.validators import MaxValueValidator, MinValueValidator

# Import Bankifi/Cashflow models
from .models import (
        Contact,
        Account,
        Transaction,
    )


# === Form Classes ===

class ContactModelForm(forms.ModelForm):
    """
    **ContactModelForm(forms.ModelForm)**

    Form used to display and validate Contact Model instances.
    """
    class Meta:
        model = Contact
        fields = [
            'name',
            'first_name',
            'last_name',
            # 'contact_id'
        ]


class AccountModelForm(forms.ModelForm):
    """
    **AccountModelForm(forms.ModelForm)**

    Form used to display and validate Account Model instances.
    """
    class Meta:
        model = Account
        fields = [
            # 'account_id',
            # 'id',
            'bank',
            'name',
            'account_number',
            'sweep_account',
            'sweep_min_balance',
        ]



class TransactionModelForm(forms.ModelForm):
    """
    **TransactionModelForm(forms.ModelForm)**

    Form used to display and validate Transaction Model instances.
    """
    class Meta:
        model = Transaction
        fields = [
            'account',
            'transaction_type',
            'description',
            'amount',
            'contact',
            'transaction_id'
        ]



