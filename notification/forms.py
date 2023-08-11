from django import forms
from.models import Notifications
class NotificationAploadForm(forms.ModelForm):
    class Meta:
        model = Notifications
        fields = "__all__"
            
