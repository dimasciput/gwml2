from django import forms


class GeologyLogForm(forms.Form):
    """
    Form of geology log of well.
    """
    # identification
    top_depth = forms.FloatField(required=False)
    bottom_depth = forms.FloatField(required=False)
    material = forms.CharField(required=False)
    geology_unit = forms.CharField(required=False)
