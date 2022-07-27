from django import forms

from yuft.labels.models import Label


class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        exclude = ('signature',)
