# Generated by Django 2.1 on 2018-09-01 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentProposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('maybe_title', models.CharField(max_length=200)),
                ('maybe_topic', models.CharField(max_length=200)),
                ('maybe_summary', models.TextField()),
                ('sub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('accepted_content', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SuggestedResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('suggestion', models.TextField()),
                ('sub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('accepted_resource', models.BooleanField(default=False)),
            ],
        ),
    ]
