# Generated by Django 4.0.6 on 2022-09-21 16:04

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('course_price', models.IntegerField()),
                ('course_discount', models.IntegerField()),
                ('course_description', froala_editor.fields.FroalaField()),
                ('slug', models.SlugField()),
            ],
        ),
    ]
