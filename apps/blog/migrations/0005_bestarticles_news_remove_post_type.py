# Generated by Django 4.2.3 on 2023-08-03 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestArticles',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.post')),
            ],
            options={
                'verbose_name': 'Best Article',
                'verbose_name_plural': 'Best Articles',
            },
            bases=('blog.post',),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.post')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
            bases=('blog.post',),
        ),
        migrations.RemoveField(
            model_name='post',
            name='type',
        ),
    ]