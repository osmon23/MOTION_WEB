# Generated by Django 4.2.3 on 2023-09-01 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('title_ky', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_ru', models.TextField(null=True, verbose_name='Description')),
                ('description_ky', models.TextField(null=True, verbose_name='Description')),
                ('description_en', models.TextField(null=True, verbose_name='Description')),
                ('graduated', models.CharField(max_length=50, verbose_name='Graduated')),
                ('graduated_ru', models.CharField(max_length=50, null=True, verbose_name='Graduated')),
                ('graduated_ky', models.CharField(max_length=50, null=True, verbose_name='Graduated')),
                ('graduated_en', models.CharField(max_length=50, null=True, verbose_name='Graduated')),
                ('years', models.CharField(max_length=50, verbose_name='Years')),
                ('years_ru', models.CharField(max_length=50, null=True, verbose_name='Years')),
                ('years_ky', models.CharField(max_length=50, null=True, verbose_name='Years')),
                ('years_en', models.CharField(max_length=50, null=True, verbose_name='Years')),
                ('mentors', models.CharField(max_length=50, verbose_name='Mentors')),
                ('mentors_ru', models.CharField(max_length=50, null=True, verbose_name='Mentors')),
                ('mentors_ky', models.CharField(max_length=50, null=True, verbose_name='Mentors')),
                ('mentors_en', models.CharField(max_length=50, null=True, verbose_name='Mentors')),
                ('work_offers', models.CharField(max_length=50, verbose_name='Work offers')),
                ('work_offers_ru', models.CharField(max_length=50, null=True, verbose_name='Work offers')),
                ('work_offers_ky', models.CharField(max_length=50, null=True, verbose_name='Work offers')),
                ('work_offers_en', models.CharField(max_length=50, null=True, verbose_name='Work offers')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='AboutUsGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='about_us/', verbose_name='Image')),
                ('file', models.FileField(blank=True, null=True, upload_to='about_us/', verbose_name='File')),
            ],
            options={
                'verbose_name': 'About us gallery',
                'verbose_name_plural': 'About us gallery',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('title_ky', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projects/', verbose_name='Image')),
                ('url', models.URLField(verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='reviews/', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='BestArticles',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.post')),
                ('best_title', models.CharField(max_length=255, verbose_name='Title')),
                ('best_title_ru', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('best_title_ky', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('best_title_en', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('best_created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
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
                ('news_title', models.CharField(max_length=255, verbose_name='Title')),
                ('news_title_ru', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('news_title_ky', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('news_title_en', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('news_created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
            bases=('blog.post',),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('name_ky', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='blog.post', verbose_name='Posts')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='PostMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(upload_to='post_media/', verbose_name='Media')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='blog.post', verbose_name='Post')),
            ],
            options={
                'verbose_name': 'Media',
                'verbose_name_plural': 'Media',
            },
        ),
        migrations.CreateModel(
            name='PostDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000, verbose_name='Description')),
                ('description_ru', models.TextField(max_length=1000, null=True, verbose_name='Description')),
                ('description_ky', models.TextField(max_length=1000, null=True, verbose_name='Description')),
                ('description_en', models.TextField(max_length=1000, null=True, verbose_name='Description')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descriptions', to='blog.post', verbose_name='Post')),
            ],
            options={
                'verbose_name': 'Description',
                'verbose_name_plural': 'Descriptions',
            },
        ),
    ]
