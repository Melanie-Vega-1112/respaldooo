# Generated by Django 5.1 on 2024-11-22 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='id',
        ),
        migrations.AddField(
            model_name='producto',
            name='Categoria',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='Descripcion',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='Material',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='Precio',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='idproducto',
            field=models.PositiveSmallIntegerField(primary_key=True, serialize=False),
        ),
    ]
