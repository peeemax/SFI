# Generated by Django 4.1.2 on 2022-11-13 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_anfitrião_filhos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anfitrião',
            name='data_casamento',
            field=models.DateField(null=True, verbose_name='Data de casamento'),
        ),
        migrations.AlterField(
            model_name='anfitrião',
            name='data_nascimento',
            field=models.DateField(verbose_name='Data de nascimento'),
        ),
    ]
