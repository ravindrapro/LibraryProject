# Generated by Django 3.2 on 2021-04-15 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_alter_book_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
