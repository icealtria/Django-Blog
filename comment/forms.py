from django import forms

from .models import Comment
import mistune

class CommentForm(forms.ModelForm):
    name = forms.CharField(
        max_length=80,
        label="Name",
        widget=forms.widgets.Input(
            attrs={
                "class": "form-control",
                'style': 'width: 60%;'
            }
        )
        )

    email = forms.EmailField(
        label="Email",
        widget=forms.widgets.EmailInput(
            attrs={
                "class": "form-control",
                'style': 'width: 60%;'
            }
        )
    )

    website = forms.URLField(
        max_length=100,
        label="Website",
        widget=forms.widgets.URLInput(
            attrs={
                "class": "form-control",
                'style': 'width: 60%;'
            }
        )
    )

    body = forms.CharField(
        label="Content",
        max_length=500,
        widget=forms.Textarea(
        attrs={
            "class": "form-control",
            'rows': 6,
            'cols': 60,
        }
    ))

    def clean_body(self):
        body = self.cleaned_data.get("body")
        if len(body) < 10:
            raise forms.ValidationError("内容太短")
        body = mistune.markdown(body)
        return body

    class Meta:
        model = Comment
        fields = ("name", "email", "website", "body")
