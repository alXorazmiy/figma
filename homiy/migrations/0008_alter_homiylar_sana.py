# Generated by Django 4.1.2 on 2022-10-12 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homiy', '0007_alter_homiylar_holat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homiylar',
            name='sana',
            field=models.DateTimeField(default='12.14.2022'),
        ),
    ]