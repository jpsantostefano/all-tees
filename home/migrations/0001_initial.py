# Generated by Django 3.2.14 on 2024-03-11 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Careers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('position', models.CharField(choices=[('Marketing', 'Marketing'), ('Sales', 'Sales'), ('Customer Service', 'Customer Service')], max_length=20)),
                ('cv', models.FileField(blank=True, null=True, upload_to='cv_uploads/')),
                ('message', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
