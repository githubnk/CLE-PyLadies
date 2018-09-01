from django.db import models
from django.utils import timezone

# Article class
class Article(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True)
    title_text = models.CharField(max_length=200)
    init_date = models.DateTimeField(
        default=timezone.now)
    pub_date = models.DateTimeField(
        blank=True, null=True)
    article_text = models.CharField(max_length=5000)
    likes = models.IntegerField(default=0)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title_text

class Comment(models.Model):
    article = models.ForeignKey(
        'newsletter.Article',
        on_delete=models.SET('deleted'),
        related_name='comments')
    author = models.CharField(max_length=200)
    comment_text = models.TextField()
    comment_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment_text

# Newsletter class
# Define Newsletter class where admin can choose articles to send:
# Top rated, most recent, by topic?
