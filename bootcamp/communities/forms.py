from django import forms

from bootcamp.communities.models import Community


class CommunityForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control ya-seed-elnas'}),
        max_length=4000)
    class Meta:
        model = Community
        fields = ['content']
