from django import forms

from hackernewsclone.models import Post, Writer


class PostForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=Writer.objects.all().values_list("name", flat=True).distinct()
    )

    class Meta:
        model = Post
        fields = ["title", "author"]

    def is_valid(self):
        title = self.data.get("title", None)
        author = self.data.get("author", None)

        if author and title:
            if Writer.objects.filter(name=author).exists():
                return True
        return False

    def save(self, *args, **kwargs):
        if self.is_valid():
            obj = Post(
                title=self.data["title"],
                author=Writer.objects.get(name=self.data["author"]),
            )
            obj.save()
            return obj
        return None


class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer
        fields = ["name"]
