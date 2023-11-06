# Generated by Django 4.2.5 on 2023-11-06 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('digital marketing', 'Digital Marketing'), ('webinars', 'Webinars'), ('sme business', 'Sme Business'), ('technology', 'Technology')], default='technology', max_length=50),
        ),
    ]
