# Generated by Django 2.1.8 on 2019-06-11 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20190610_2221'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'), ('can_see_borrowed', 'See all borrowers'))},
        ),
    ]