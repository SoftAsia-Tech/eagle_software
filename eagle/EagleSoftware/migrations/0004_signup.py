# Generated by Django 5.0.3 on 2024-03-23 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EagleSoftware', '0003_delete_mymodel_remove_choice_choice_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
