from django import forms
from.models import Vendor
class DisplayVendor(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = "__all__"
            
