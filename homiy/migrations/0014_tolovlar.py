# Generated by Django 4.1.2 on 2022-10-13 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homiy', '0013_talabalar_phono'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tolovlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.CharField(default='13.10.2022', max_length=200)),
                ('homiy_id', models.IntegerField()),
                ('talaba_id', models.IntegerField()),
                ('summa', models.IntegerField()),
            ],
        ),
    ]
