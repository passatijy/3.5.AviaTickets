from django import forms

from .widgets import AjaxInputWidget
from .models import City


class SearchTicket(forms.Form):
    # Добавьте здесь поля, описанные в задании
    city_from = forms.CharField(widget=AjaxInputWidget('api/city_ajax', attrs={'class': 'inline right-margin'}))
    city_to = forms.CharField(max_length=30)
    date_departure = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
