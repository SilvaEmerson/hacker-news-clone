from django import forms
from django.contrib.auth.models import User

from hackernewsclone.models import Post


class PostForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=User.objects.all().values_list("username", flat=True).distinct()
    )

    class Meta:
        model = Post
        fields = ["title", "author", "content"]

    def is_valid(self):
        title = self.data.get("title", None)
        author = self.data.get("author", None)
        content = self.data.get("content", None)

        if author and title and content:
            if User.objects.filter(username=author).exists() and len(content) > 0:
                return True
        return False

    def save(self, *args, **kwargs):
        if self.is_valid():
            obj = Post(
                title=self.data["title"],
                author=User.objects.get(username=self.data["author"]),
                content=self.data["content"],
            )
            obj.save()
            return obj
        return None


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "email"]
