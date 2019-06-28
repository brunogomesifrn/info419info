# Generated by Django 2.2.2 on 2019-06-28 12:22
# Generated by Django 2.2.2 on 2019-06-28 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100, verbose_name='tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=100, verbose_name='produtos')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('preco', models.FloatField(max_length=100, verbose_name='preco')),
                ('descricao', models.CharField(max_length=100, verbose_name='descricao')),
                ('quantidade', models.IntegerField(verbose_name='quantidade')),
                ('imagem', models.ImageField(upload_to='img', verbose_name='imagem')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Tipo')),
            ],
        ),
    ]