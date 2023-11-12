# Generated by Django 4.2.7 on 2023-11-11 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brags', '0002_subscription_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
        migrations.AlterField(
            model_name='brag',
            name='duration',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]