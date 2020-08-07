from django import forms
from gwml2.models.hydrogeological_unit.gw_aquifer import AquiferTypeTerm

CONFINMENT_TYPE = (
    ('CONFINMENT TYPE 1', 'CONFINMENT TYPE 1'),
    ('CONFINMENT TYPE 2', 'CONFINMENT TYPE 2')
)


class HydrogeologyForm(forms.Form):
    """
    Form of hydro geology of well and spring
    """
    # Aquifer
    aquifer_name = forms.CharField()
    aquifer_material = forms.CharField()
    aquifer_type = forms.ModelChoiceField(
        queryset=AquiferTypeTerm.objects.all(),
        empty_label='------')
    thickness = forms.FloatField()
    confinement = forms.ChoiceField(
        required=False,
        choices=CONFINMENT_TYPE,
        widget=forms.Select())

    # wells only
    porosity = forms.FloatField()
    hydraulic_conductivity = forms.FloatField()
    transmissivity = forms.FloatField()
    specific_storage = forms.FloatField()
    specific_yield = forms.FloatField()
    specific_capacity = forms.FloatField()
    test_type = forms.CharField()
