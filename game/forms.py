from django import forms
from .models import BankModel

class NewBankForm(forms.ModelForm):
    """Form to create new club."""

    class Meta:
        """Form options."""

        model = BankModel
        fields = ['name', 'fullName']
