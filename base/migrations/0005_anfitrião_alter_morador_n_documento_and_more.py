# Generated by Django 4.1.2 on 2022-11-13 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_morador_estudando_morador_grau_parentesco_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anfitrião',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=60, verbose_name='Nome Completo')),
                ('data_nascimento', models.DateTimeField(verbose_name='Data de nascimento')),
                ('rg', models.IntegerField(max_length=7, verbose_name='Número do RG')),
                ('cpf', models.IntegerField(max_length=11, verbose_name='Número do CPF')),
                ('data_casamento', models.DateTimeField(verbose_name='Data de casamento')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Sexo')),
                ('nome_pai', models.CharField(max_length=60, verbose_name='Nome do Pai')),
                ('nome_mãe', models.CharField(max_length=60, verbose_name='Nome da Mãe')),
                ('naturalidade', models.CharField(max_length=60, verbose_name='Cidade de origem')),
                ('estado_civil', models.CharField(choices=[('Solteiro/a', 'Solteiro/a'), ('Casado/a', 'Casado/a'), ('Viúvo/a', 'Viúvo/a'), ('Separado/a', 'Separado/a'), ('Outros', 'Outros')], max_length=17, verbose_name='Estado civil')),
                ('escolaridade', models.CharField(choices=[('Fundamental', 'Fundamental'), ('Médio', 'Médio'), ('Superior Inc.', 'Superior Inc.'), ('Superior Completo', 'Superior Completo'), ('Sem escolaridade', 'Sem escolaridade')], max_length=17, verbose_name='Escolaridade')),
                ('tipo_residencia', models.CharField(choices=[('Própria', 'Própria'), ('Alugada', 'Alugada'), ('Moro com Parentes', 'Moro com Parentes'), ('Outro', 'Outro')], max_length=17, verbose_name='Tipo de Residência')),
            ],
        ),
        migrations.AlterField(
            model_name='morador',
            name='n_documento',
            field=models.IntegerField(max_length=11, verbose_name='Número do documento'),
        ),
        migrations.AlterField(
            model_name='morador',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=10, verbose_name='Sexo'),
        ),
    ]
