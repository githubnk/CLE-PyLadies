from django import forms

from .models import Article, Comment

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title_text', 'article_text')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'comment_text',)
