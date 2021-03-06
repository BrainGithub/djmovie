# Generated by Django 2.0.5 on 2018-08-23 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_markdown.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviename', models.CharField(blank=True, max_length=64)),
                ('doubanlink', models.CharField(blank=True, max_length=256, null=True)),
                ('doubanscore', models.CharField(blank=True, max_length=64, null=True)),
                ('doubancounter', models.IntegerField(blank=True, null=True)),
                ('imdblink', models.CharField(blank=True, max_length=256, null=True)),
                ('imdbscore', models.CharField(blank=True, max_length=64, null=True)),
                ('imdbcounter', models.IntegerField(blank=True, null=True)),
                ('nomovielink', models.CharField(blank=True, max_length=256, null=True)),
                ('nomoviescore', models.CharField(blank=True, max_length=64, null=True)),
                ('nomoviecounter', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=64, null=True)),
                ('dateyear', models.CharField(blank=True, max_length=64, null=True)),
                ('actor', models.CharField(blank=True, max_length=256, null=True)),
                ('director', models.CharField(blank=True, max_length=256, null=True)),
                ('style', models.CharField(blank=True, max_length=64, null=True)),
                ('movieaddress', models.CharField(blank=True, max_length=256, null=True)),
                ('downloadlink', models.CharField(blank=True, max_length=256, null=True)),
                ('counter', models.IntegerField(blank=True, null=True)),
                ('original', models.CharField(blank=True, max_length=256, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='full/')),
                ('spidertime', models.DateTimeField(auto_now_add=True, null=True)),
                ('aboutmovie', models.CharField(blank=True, max_length=256, null=True)),
                ('language', models.CharField(blank=True, max_length=64, null=True)),
                ('dyttsearch', models.CharField(blank=True, max_length=256, null=True)),
                ('dyttdetail', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieComent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comment', django_markdown.models.MarkdownField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MovieHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('marked', models.IntegerField(blank=True, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MovieSpider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_tag', models.CharField(blank=True, max_length=512, null=True)),
                ('moviename', models.CharField(blank=True, max_length=64, null=True)),
                ('moviedetailurl', models.CharField(blank=True, max_length=512, null=True)),
                ('movieimgurl', models.CharField(blank=True, max_length=512, null=True)),
                ('movieaddtime', models.DateTimeField(auto_now_add=True)),
                ('moviespiderornot', models.IntegerField(default=0)),
                ('country', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
    ]
