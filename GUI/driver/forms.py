from django import forms

class DriverForm(forms.Form):
    minDate = forms.DateField(label="Min Date")
    maxDate = forms.DateField(label="Max Date")
    minScore = forms.FloatField(label="Min Score")
    maxScore = forms.FloatField(label="Max Score")
    limit = forms.IntegerField(label="Limit", initial=50)
    offset = forms.IntegerField(label="Offset", initial=0)
