# Generated by Django 4.2.3 on 2023-08-02 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_coursesimage_image_alter_mentor_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.CharField(max_length=255, verbose_name='Format')),
                ('description', models.TextField(verbose_name='Description')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='format', to='courses.course')),
            ],
            options={
                'verbose_name': 'Format',
                'verbose_name_plural': 'Formats',
            },
        ),
    ]