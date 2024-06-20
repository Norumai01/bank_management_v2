from django import forms
from customers.models import Account

class BalanceForm(forms.Form):
    account = forms.ModelChoiceField(queryset=Account.objects.all(), label="Select Account")