# Generated by Django 4.1.2 on 2022-10-12 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homiy', '0005_homiylar_nomi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homiylar',
            name='holat',
            field=models.CharField(choices=[('yn', 'yangi'), ('md', 'moderatsiyada'), ('tq', 'tasdiqlangan'), ('bq', 'bekor qilingan')], default='yn', max_length=2),
        ),
    ]
