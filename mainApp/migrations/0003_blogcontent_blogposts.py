# Generated by Django 3.2 on 2021-11-29 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20211129_0637'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=250)),
                ('main_image', models.ImageField(upload_to='blogPost/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'All Blog Posts',
                'verbose_name_plural': 'All Blog Posts',
            },
        ),
        migrations.CreateModel(
            name='BlogContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('blog_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.blogposts')),
            ],
        ),
    ]