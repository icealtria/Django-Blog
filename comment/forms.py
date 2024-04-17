from django import forms

from .models import Comment
import mistune

FORM_CONTROL_STYLE = {
    "class": "form-control",
    "style": "width: 60%;"
}

class CommentForm(forms.ModelForm):
    name = forms.CharField(
        max_length=80,
        label="Name",
        widget=forms.widgets.Input(attrs=FORM_CONTROL_STYLE)
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.widgets.EmailInput(attrs=FORM_CONTROL_STYLE)
    )

    website = forms.URLField(
        max_length=100,
        label="Website",
        widget=forms.widgets.URLInput(attrs=FORM_CONTROL_STYLE)
    )

    body = forms.CharField(
        label="Content",
        max_length=500,
        widget=forms.Textarea(attrs={**FORM_CONTROL_STYLE, "rows": 6, "cols": 60})
    )

    def clean_body(self):
        body = self.cleaned_data.get("body")
        if len(body) < 10:
            raise forms.ValidationError("内容太短")
        body = mistune.markdown(body)
        return body

    class Meta:
        model = Comment
        fields = ("name", "email", "website", "body")
