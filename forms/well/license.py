from django import forms


class LicenseForm(forms.Form):
    """
    Form of license.
    """
    id = forms.CharField(label='License Number')
    valid_from = forms.DateField()
    valid_to = forms.DateField()
    description = forms.CharField(widget=forms.Textarea, required=False)
