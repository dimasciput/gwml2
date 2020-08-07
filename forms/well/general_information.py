from django import forms


class GeneralInformationForm(forms.Form):
    """
    Form of general information of well.
    """
    # identification
    id = forms.CharField()
    name = forms.CharField()
    feature_type = forms.CharField()

    # Location Information
    latitude = forms.FloatField(help_text='latitude of well', min_value=-90, max_value=90)
    longitude = forms.FloatField(help_text='longitude of well', min_value=-180, max_value=180)
    country = forms.CharField(help_text='country of well')
    address = forms.CharField(
        widget=forms.Textarea, required=False,
        help_text='country of well')
    elevation = forms.CharField(help_text='elevation of well')

    # Summary Information
    photo = forms.FileField(required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
