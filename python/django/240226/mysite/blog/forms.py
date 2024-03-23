from django import forms
from .models import Post


class PostForm(forms.ModelForm):  # PostForm은 여러분이 원하는 이름으로 바꿔도 됩니다.
    title = forms.CharField(max_length=100)
    contents = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ["title", "contents", "main_image"]
        # fields = '__all__'