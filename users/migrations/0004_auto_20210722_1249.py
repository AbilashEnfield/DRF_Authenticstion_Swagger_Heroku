# Generated by Django 3.2.5 on 2021-07-22 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='place',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
