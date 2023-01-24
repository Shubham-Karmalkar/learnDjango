# Generated by Django 4.1.5 on 2023-01-24 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
            preserve_default=False,
        ),
    ]