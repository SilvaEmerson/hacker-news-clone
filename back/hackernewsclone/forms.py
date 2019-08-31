from django import forms

from hackernewsclone.models import Post, Writer


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "author"]
        author = forms.ModelMultipleChoiceField(
            queryset=Writer.objects.all(), to_field_name="name"
        )


class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer
        fields = ["name"]
