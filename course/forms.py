from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Level, Programme


class CreateInstituteForm(forms.Form):
    institute_name = forms.CharField(
        label="Institute Name",
        max_length=300,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter institute name",
            }
        ),
        required=True,
    )
    level = forms.ModelMultipleChoiceField(
        label="Levels",
        queryset=Level.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(CreateInstituteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))


class CreateLevelForm(forms.Form):
    level_name = forms.CharField(
        label="Level Name",
        max_length=300,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter level name"}
        ),
        required=True,
    )
    programme = forms.ModelMultipleChoiceField(
        label="Programmes",
        queryset=Programme.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(CreateLevelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))
