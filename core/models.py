from django.db import models
from django.utils import timezone

# Create your models here.
class SuggestedResource(models.Model):
    user = models.CharField(max_length=200)
    email = models.EmailField()
    suggestion = models.TextField()
    sub_date = models.DateTimeField(
        default=timezone.now)
    accepted_resource = models.BooleanField(default=False)

    def submit(self):
        self.sub_date = timezone.now()
        self.save()

    def approve(self):
        self.accepted_resource = True
        self.save()

    def __str__(self):
        return self.suggestion


class ContentProposal(models.Model):
    try:
        user = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True)
    except:
        user = models.CharField(max_length=200)
    email = models.EmailField()
    maybe_title = models.CharField(max_length=200)
    maybe_topic = models.CharField(max_length=200)
    maybe_summary = models.TextField()
    sub_date = models.DateTimeField(
        default=timezone.now)
    accepted_content = models.BooleanField(default=False)

    def submit(self):
        self.sub_date = timezone.now()
        self.save()

    def approve(self):
        self.accepted_content = True
        self.save()

    def __str__(self):
        return self.maybe_title
