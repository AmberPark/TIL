from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'title',
                'class':'my-title form-control',
            }
        ),
        error_messages={
            'required':'please type',
        }
    )
    overview = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder':'Overview',
                'class':'my-overview form-control',
                'rows':10,
                'cols':30,
            }
        ),
        error_messages={
            'required':'please type',
        }
    )

    class Meta:
        model = Movie
        fields = '__all__'